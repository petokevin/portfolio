from django import template
from django.utils.html import format_html
from django.utils.safestring import mark_safe

register = template.Library()
# Small, local outline icons: no external fonts or scripts required.
PATHS = {
    'arrow': '<path d="M7 17 17 7M7 7h10v10"/>',
    'right': '<path d="M4 12h16m-6-6 6 6-6 6"/>',
    'down': '<path d="m6 9 6 6 6-6"/>',
    'code': '<path d="m7 7-5 5 5 5m10-10 5 5-5 5m-3-13-4 20"/>',
    'terminal': '<rect x="2" y="3" width="20" height="18" rx="3"/><path d="m6 8 4 4-4 4m7 0h5"/>',
    'database': '<ellipse cx="12" cy="5" rx="8" ry="3"/><path d="M4 5v14c0 4 16 4 16 0V5M4 12c0 4 16 4 16 0"/>',
    'layers': '<path d="m12 2 10 5-10 5L2 7l10-5ZM2 12l10 5 10-5M2 17l10 5 10-5"/>',
    'send': '<path d="m22 2-7 20-4-9-9-4L22 2ZM11 13 22 2"/>',
    'palette': '<path d="M12 3a9 9 0 1 0 0 18h1a2 2 0 0 0 1-4 2 2 0 0 1 1-4h3c5 0 3-10-6-10Z"/><path d="M7 9h.01M11 6h.01M16 8h.01M6 14h.01"/>',
    'tasks': '<rect x="4" y="3" width="16" height="19" rx="2"/><path d="M9 2h6v4H9zM8 11h1m3 0h4M8 16h1m3 0h4"/>',
    'workflow': '<rect x="8" y="2" width="8" height="5" rx="1"/><rect x="2" y="17" width="7" height="5" rx="1"/><rect x="15" y="17" width="7" height="5" rx="1"/><path d="M12 7v5H5v5m7-5h7v5"/>',
    'table': '<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M3 15h18M9 3v18"/>',
    'file': '<path d="M14 2H5v20h14V7l-5-5Zm0 0v6h5M8 12h8m-8 4h8"/>',
    'briefcase': '<rect x="2" y="7" width="20" height="14" rx="2"/><path d="M8 7V3h8v4M2 12c6 4 14 4 20 0m-10 0v4"/>',
    'rotate': '<path d="M20 7a9 9 0 0 0-15-3L2 7m0-5v5h5M4 17a9 9 0 0 0 15 3l3-3m0 5v-5h-5"/>',
    'search': '<circle cx="10" cy="10" r="7"/><path d="m15 15 7 7"/>',
    'users': '<circle cx="9" cy="7" r="4"/><path d="M2 21v-3a7 7 0 0 1 14 0v3m0-18a4 4 0 0 1 0 8m3 3c3 1 3 4 3 7"/>',
    'calendar': '<rect x="3" y="5" width="18" height="17" rx="2"/><path d="M7 2v6m10-6v6M3 11h18m-14 5h3m4 0h3"/>',
    'shield': '<path d="m12 2 9 4v6c0 5-9 10-9 10S3 17 3 12V6l9-4Z"/><path d="m8 12 3 3 5-6"/>',
    'rocket': '<path d="M9 15c-3-7 5-13 13-13 0 8-6 16-13 13ZM9 9H5l-3 6h7m6 0v4l-6 3v-7M3 21l3-3"/><circle cx="16" cy="8" r="2"/>',
    'check': '<circle cx="12" cy="12" r="9"/><path d="m7 12 3 3 7-7"/>',
    'plug': '<path d="m8 3 4 4m4-4 4 4M7 5l12 12m-9-9-5 5a5 5 0 0 0 7 7l5-5M5 19l-3 3"/>',
    'sparkles': '<path d="m12 3 2.5 6.5L21 12l-6.5 2.5L12 21l-2.5-6.5L3 12l6.5-2.5L12 3ZM20 2v4m-2-2h4"/>',
    'chart': '<path d="M3 3v18h19M7 16v-5m5 5V7m5 9V4"/>',
    'graduation': '<path d="m12 3 11 6-11 6L1 9l11-6ZM5 12v6c4 3 10 3 14 0v-6m4-3v8"/>',
    'mail': '<rect x="2" y="4" width="20" height="16" rx="3"/><path d="m2 6 10 7L22 6"/>',
    'pin': '<path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/>',
    'folder': '<path d="M2 6a2 2 0 0 1 2-2h5l3 3h8a2 2 0 0 1 2 2v11H2V6Z"/>',
    'clock': '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    'cloud-sun': '<path d="M12 3v2m5-1-1.4 1.4M21 10h-2M5 10H3m5.4-4.6L7 4"/><path d="M16 15.5A4.5 4.5 0 0 0 7.3 14 3.5 3.5 0 1 0 6 21h10a3 3 0 0 0 0-6Z"/><path d="M9 9a4 4 0 0 1 7.7 1.5"/>',
}


@register.simple_tag
def icon(name):
    return format_html('<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.65" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{}</svg>', mark_safe(PATHS.get(name, PATHS['code'])))
