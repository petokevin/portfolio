(() => {
  const tabs = document.querySelector('.editor-tabs');
  const links = [...tabs.querySelectorAll('[data-file]')];
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

  const positionIndicator = () => {
    const selected = tabs.querySelector('.active');
    if (!selected) return;
    tabs.style.setProperty('--tab-left', `${selected.offsetLeft}px`);
    tabs.style.setProperty('--tab-width', `${selected.offsetWidth}px`);
  };

  const selectSection = (hash, revealTab = false) => {
    const selected = links.find(link => link.hash === hash);
    if (!selected) return;
    links.forEach(link => {
      const active = link === selected;
      link.classList.toggle('active', active);
      if (active) link.setAttribute('aria-current', 'location');
      else link.removeAttribute('aria-current');
    });
    document.querySelector('#current-file').textContent = selected.dataset.file;
    document.querySelector('.status-module').textContent = selected.dataset.file;
    positionIndicator();
    if (revealTab) {
      const left = selected.offsetLeft;
      const right = left + selected.offsetWidth;
      if (left < tabs.scrollLeft || right > tabs.scrollLeft + tabs.clientWidth) {
        tabs.scrollTo({
          left: left - (tabs.clientWidth - selected.offsetWidth) / 2,
          behavior: reducedMotion.matches ? 'instant' : 'smooth',
        });
      }
    }
  };

  // Select immediately; intervening sections during smooth scrolling must not
  // briefly take over the tab the visitor has just chosen.
  document.querySelectorAll('a[href^="#"]').forEach(link => {
    link.addEventListener('click', event => {
      if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
      selectSection(link.hash, true);
    });
  });
  window.addEventListener('hashchange', () => selectSection(location.hash || '#rolam', true));
  window.addEventListener('resize', positionIndicator);
  selectSection(location.hash || '#rolam', true);
  requestAnimationFrame(() => {
    positionIndicator();
    tabs.setAttribute('data-ready', '');
  });
  document.fonts.ready.then(positionIndicator);

  if ('IntersectionObserver' in window && !reducedMotion.matches) {
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.05 });
    document.documentElement.classList.add('js-motion');
    document.querySelectorAll('.reveal').forEach(element => observer.observe(element));
  }

  const portrait = document.querySelector('.portrait-wrap');
  if (portrait) {
    let portraitTimer;
    const startPortraitSwap = () => {
      window.clearTimeout(portraitTimer);
      portrait.classList.remove('is-swapped');
      portrait.classList.add('is-scanning');
      portraitTimer = window.setTimeout(() => {
        portrait.classList.add('is-swapped');
      }, reducedMotion.matches ? 0 : 1120);
    };
    const resetPortraitSwap = () => {
      window.clearTimeout(portraitTimer);
      portrait.classList.remove('is-scanning', 'is-swapped');
    };

    portrait.addEventListener('pointerenter', startPortraitSwap);
    portrait.addEventListener('pointerleave', resetPortraitSwap);
    portrait.addEventListener('mouseenter', startPortraitSwap);
    portrait.addEventListener('mouseleave', resetPortraitSwap);
    portrait.addEventListener('focusin', startPortraitSwap);
    portrait.addEventListener('focusout', resetPortraitSwap);
  }

  const livePanel = document.querySelector('[data-live-panel]');
  if (!livePanel) return;

  const timeElement = livePanel.querySelector('[data-live-time]');
  const dateElement = livePanel.querySelector('[data-live-date]');
  const temperatureElement = livePanel.querySelector('[data-weather-temp]');
  const summaryElement = livePanel.querySelector('[data-weather-summary]');
  const windElement = livePanel.querySelector('[data-weather-wind]');
  const humidityElement = livePanel.querySelector('[data-weather-humidity]');
  const timeZone = 'Europe/Budapest';

  const timeFormatter = new Intl.DateTimeFormat('hu-HU', {
    timeZone,
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit',
  });
  const dateFormatter = new Intl.DateTimeFormat('hu-HU', {
    timeZone,
    weekday: 'long',
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  });

  const updateHungarianTime = () => {
    const now = new Date();
    timeElement.textContent = timeFormatter.format(now);
    dateElement.textContent = dateFormatter.format(now);
    timeElement.setAttribute('datetime', now.toISOString());
  };

  const weatherDescriptions = {
    0: 'Derült',
    1: 'Többnyire derült',
    2: 'Részben felhős',
    3: 'Borult',
    45: 'Köd',
    48: 'Zúzmarás köd',
    51: 'Gyenge szitálás',
    53: 'Szitálás',
    55: 'Erős szitálás',
    56: 'Ónos szitálás',
    57: 'Erős ónos szitálás',
    61: 'Gyenge eső',
    63: 'Eső',
    65: 'Erős eső',
    66: 'Ónos eső',
    67: 'Erős ónos eső',
    71: 'Gyenge havazás',
    73: 'Havazás',
    75: 'Erős havazás',
    77: 'Hódara',
    80: 'Gyenge zápor',
    81: 'Zápor',
    82: 'Erős zápor',
    85: 'Gyenge hózápor',
    86: 'Hózápor',
    95: 'Zivatar',
    96: 'Zivatar jégesővel',
    99: 'Erős zivatar jégesővel',
  };

  const updateWeather = async () => {
    const url = 'https://api.open-meteo.com/v1/forecast?latitude=47.4979&longitude=19.0402&current=temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m&timezone=Europe%2FBudapest';
    try {
      const response = await fetch(url, { cache: 'no-store' });
      if (!response.ok) throw new Error(`Weather request failed: ${response.status}`);
      const data = await response.json();
      const current = data.current;
      if (!current) throw new Error('Weather response did not include current data');

      temperatureElement.textContent = `${Math.round(current.temperature_2m)}°C`;
      summaryElement.textContent = weatherDescriptions[current.weather_code] || 'Aktuális időjárás';
      windElement.textContent = `Szél: ${Math.round(current.wind_speed_10m)} km/h`;
      humidityElement.textContent = `Páratartalom: ${Math.round(current.relative_humidity_2m)}%`;
      livePanel.dataset.weatherState = 'ready';
    } catch (error) {
      summaryElement.textContent = 'Időjárás most nem elérhető';
      livePanel.dataset.weatherState = 'error';
    }
  };

  updateHungarianTime();
  updateWeather();
  window.setInterval(updateHungarianTime, 1000);
  window.setInterval(updateWeather, 10 * 60 * 1000);
})();
