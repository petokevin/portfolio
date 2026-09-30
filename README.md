# Pető Márk Kevin — IT Project Manager portfólió

Magyar nyelvű, reszponzív, egylapos Django portfólió PyCharm ihlette, sötét IDE-megjelenéssel. A felső szerkesztőfülek a hét szekcióra navigálnak. Kattintáskor az animált kijelölés az új fülre kerül; a fájlnévjelzés és a böngésző előre/vissza navigációja ugyanazt a kiválasztást követi. Bal oldali menü nincs. A Python-konzol bemutatkozó, statikus tartalom, nem futtat kódot. A projekt önálló: a szülőmappában található háztartási alkalmazást nem módosítja.

## Megnyitás ezen a gépen

A helyi előnézet címe: **http://127.0.0.1:8001/**

Indítás Windows-on: dupla kattintás a projekt `start.bat` fájljára, vagy PowerShellből a projektmappában:

```powershell
.\start.bat
```

Indítás macOS-en: dupla kattintás a projekt `start.command` fájljára, vagy a projektmappából:

```sh
./start.command
```

Ez a saját `.venv` környezetet használja, vagy annak hiányában a szülőmappában már meglévőt. A 8001-es portot választja, hogy a másik alkalmazás 8000-es portja szabad maradjon. A terminált hagyd nyitva; leállítás: Ctrl+C. Ha már fut az előnézet, nem kell még egyszer elindítani.

## Önálló telepítés

Python 3.10 vagy újabb szükséges. A `portfolio` projektmappában:

Windows:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py runserver 127.0.0.1:8001
```

macOS/Linux:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py runserver 127.0.0.1:8001
```

Másik porthoz például: `python manage.py runserver 127.0.0.1:8002`.

Nincs szükség adatbázisra, migrációkra, adminfiókra, frontend buildre vagy külső szolgáltatásra. A portré, ikonok, stílusok és JavaScript helyi fájlokból töltődnek be.

## Tartalom szerkesztése

- `main/data.py`: 12 projekt és feladatlistáik, 12 technológia, az eredeti PM kompetencialista, 3 munkahely és 3 képzés.
- `main/templates/main/index.html`: bemutatkozás, statisztikák, terminál és kapcsolati szekció.
- `main/templates/main/base.html`: menü, metaadatok, lábléc.
- `main/static/main/css/style.css`: színek, elrendezések, reszponzivitás, animációk.
- `main/static/main/js/main.js`: animált fülkijelölés, aktív szekció jelzése, megjelenési animációk.
- `main/static/main/img/profile.jpg`: a megadott eredeti portré; fekete-fehér megjelenítés és kivágás CSS-sel.
- `main/templatetags/icons.py`: helyben renderelt SVG ikonok.

Az alapértelmezett e-mail-cím: **peto.kevinwork@gmail.com**. Felülírható a `PORTFOLIO_EMAIL` környezeti változóval. LinkedIn-profil nem lett megadva, ezért ilyen link nem jelenik meg; a `PORTFOLIO_LINKEDIN` teljes HTTPS URL megadásával hozzáadható.

A kapcsolatfelvétel `mailto:` linkkel a látogató levelezőjét nyitja meg. Nincs szerveroldali levélküldés vagy üzenettárolás.

## Ellenőrzés

```sh
python manage.py check
```

A projektkártyák rövid leírást és címkéket mutatnak, feladatlisták nélkül. A projektmenedzsment szekció három fókuszterületre egyszerűsítve jelenik meg. A finom animációk követik a csökkentett mozgás rendszerbeállítását.

## Üzemeltetés

A mellékelt konfiguráció helyi fejlesztéshez készült, és csak loopback címeken szolgál ki. Nyilvános üzemeltetéshez külön telepítési konfiguráció szükséges: egyedi `DJANGO_SECRET_KEY`, `DJANGO_DEBUG=0`, megfelelő `DJANGO_ALLOWED_HOSTS`, HTTPS, WSGI szerver és statikus fájlkiszolgálás (`collectstatic`). Az oldal nem lett nyilvánosan publikálva.

Designreferencia: [PyCharm felhasználói felülete](https://www.jetbrains.com/help/pycharm/guided-tour-around-the-user-interface.html). Saját PMK arculat, Python-szintaxisú színek és normál, jól olvasható törzsszöveg.
