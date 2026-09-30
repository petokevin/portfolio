"""A portfólió szerkeszthető tartalma; nem igényel adatbázist."""

TECHNOLOGIES = [
    ('Python', 'python', 'Fejlesztés', 'blue'),
    ('Django', 'django', 'Web framework', 'green'),
    ('SQL', 'sql', 'Adatkezelés', 'purple'),
    ('Docker', 'docker', 'Konténerizáció', 'blue'),
    ('Postman', 'postman', 'API tesztelés', 'orange'),
    ('HTML', 'html', 'Webfejlesztés', 'orange'),
    ('CSS', 'css', 'Megjelenés', 'blue'),
    ('Redmine', 'redmine', 'Projektkövetés', 'red'),
    ('ServiceNow', 'servicenow', 'IT folyamatok', 'green'),
    ('Microsoft Visio', 'visio', 'Folyamatábrák', 'purple'),
    ('Microsoft Excel', 'excel', 'Adatelemzés', 'green'),
    ('Microsoft Word', 'word', 'Dokumentáció', 'blue'),
]

COMPETENCIES = [
    ('IT Project Management', 'briefcase'), ('Agile', 'rotate'),
    ('Requirements Analysis', 'search'), ('Technical Specification', 'file'),
    ('Stakeholder Management', 'users'), ('Project Planning', 'calendar'),
    ('Risk Management', 'shield'), ('Change Management', 'rotate'),
    ('Release Management', 'rocket'), ('UAT & Testing', 'check'),
    ('Process Optimization', 'workflow'), ('API & System Integration', 'plug'),
    ('Cross-functional Team Leadership', 'users'), ('Multi-project Management', 'layers'),
]

PROJECTS = [
    {'name': 'Regisztrációs rendszer', 'category': 'Alkalmazásfejlesztés', 'icon': 'registration', 'color': 'blue',
     'description': 'Eseményregisztrációs folyamatok koordinálása és fejlesztési igények kezelése.',
     'tags': ['Requirements', 'UI/UX', 'Koordináció']},
    {'name': 'SharePoint–Drupal integráció', 'category': 'Rendszerintegráció', 'icon': 'sharepoint-drupal', 'color': 'cyan',
     'description': 'SharePoint tartalmak Drupalból történő elérésének előkészítése.',
     'tags': ['Graph API', 'Entra ID', 'API']},
    {'name': 'Behajtási és parkolási rendszer', 'category': 'Folyamatfejlesztés', 'icon': 'parking', 'color': 'cyan',
     'description': 'Behajtási engedélyekhez kapcsolódó folyamatok fejlesztése.',
     'tags': ['Folyamattervezés', 'Specifikáció']},
    {'name': 'Névjegy / CAFM integráció', 'category': 'Rendszerintegráció', 'icon': 'cafm', 'color': 'blue',
     'description': 'Dolgozói adatok és CAFM rendszer közötti adatkapcsolat támogatása.',
     'tags': ['Adatkapcsolat', 'CAFM', 'Integráció']},
    {'name': 'Immich rendszer', 'category': 'Infrastruktúra', 'icon': 'immich', 'color': 'purple',
     'description': 'Belső kép- és médiakezelő rendszer bevezetésének támogatása.',
     'tags': ['HTTPS', 'Entra ID', 'SIEM']},
    {'name': 'Kedvezmények portál', 'category': 'Web & UX', 'icon': 'discounts', 'color': 'purple',
     'description': 'Hallgatói és dolgozói kedvezmények portálfelületének előkészítése.',
     'tags': ['Figma', 'UI/UX', 'Specifikáció']},
    {'name': 'Innovációs portál', 'category': 'Web & UX', 'icon': 'innovation', 'color': 'cyan',
     'description': 'Egyetemi innovációs weboldal továbbfejlesztésének koordinálása.',
     'tags': ['Webfejlesztés', 'Requirements']},
    {'name': 'Konferencia / rendezvényoldalak', 'category': 'Alkalmazásfejlesztés', 'icon': 'conference', 'color': 'blue',
     'description': 'Rendezvényoldalak és regisztrációs folyamatok előkészítése.',
     'tags': ['Tervezés', 'Ütemezés', 'Koordináció']},
    {'name': 'Redmine fejlesztések', 'category': 'Folyamatfejlesztés', 'icon': 'redmine-project', 'color': 'blue',
     'description': 'Projekt- és feladatkezelési folyamatok optimalizálása Redmine-ban.',
     'tags': ['Redmine', 'Agile', 'Optimalizálás']},
    {'name': 'Webes és portálfejlesztések', 'category': 'Web & UX', 'icon': 'web-portals', 'color': 'purple',
     'description': 'Weboldalak és belső portálok fejlesztésének támogatása.',
     'tags': ['UI/UX', 'Release', 'Tesztelés']},
    {'name': 'Impakt faktor számláló rendszer', 'category': 'Adat & elemzés', 'icon': 'impact', 'color': 'cyan',
     'description': 'Publikációs adatok és impakt faktor számítási logika támogatása.',
     'tags': ['Üzleti elemzés', 'Adatok', 'Tesztelés']},
    {'name': 'Password értesítési rendszer', 'category': 'Rendszerintegráció', 'icon': 'password', 'color': 'blue',
     'description': 'Jelszólejárati értesítések és kapcsolódó adatforrások fejlesztése.',
     'tags': ['Értesítések', 'Neptun', 'Specifikáció']},
]

EXPERIENCE = [
    {'role': 'IT Project Manager', 'organization': 'Pécsi Tudományegyetem', 'department': 'Kancellária / Alkalmazásfejlesztési Osztály', 'date': '2025 — jelenleg', 'current': True, 'logo': 'pte.png',
     'tasks': ['IT-fejlesztési projektek teljes körű koordinálása', 'Igényfelmérés, funkcionális és technikai specifikációk készítése', 'Fejlesztőkkel és üzleti szereplőkkel való egyeztetés', 'Feladatok priorizálása és tesztelések koordinálása', 'Release-ek támogatása és több párhuzamos projekt kezelése']},
    {'role': 'Elemző / Fejlesztő', 'organization': 'Szerencsejáték Zrt.', 'department': '', 'date': '2024 — 2025', 'logo': 'szerencsejatek.png',
     'tasks': ['Üzleti folyamatok elemzése és fejlesztési igények kezelése', 'Terv–tény monitorozás és fejlesztési tervek készítése', 'Üzleti és technikai területek közötti együttműködés']},
    {'role': 'Adatmenedzsment gyakornok', 'organization': 'E.ON Dél-dunántúli Áramhálózati Zrt.', 'department': '', 'date': '2021 — 2024', 'logo': 'eon.svg',
     'tasks': ['Adatok kezelése, elemzése és riportok készítése', 'Excel, Power BI és SAP-alapú adatlekérdezések', 'Adatminőség javítása és üzleti riportok támogatása']},
]

EDUCATION = [
    {'degree': 'MSc', 'title': 'Gazdaságinformatikus', 'school': 'Gábor Dénes Egyetem', 'date': '2025 — jelenleg', 'logo': 'gde.png',
     'topics': 'Informatikai rendszerek · Adatkezelés · Üzleti folyamatok · Technológiai megoldások · Gazdaságinformatika'},
    {'degree': 'BSc', 'title': 'Gazdálkodási és menedzsment', 'school': 'Pécsi Tudományegyetem · Közgazdaságtudományi Kar', 'date': '2020 — 2024', 'logo': 'pte.png',
     'topics': 'Vállalati gazdaságtan · Menedzsment · Projektmenedzsment · Folyamatmenedzsment · Döntéstámogatás'},
    {'degree': 'FOSZK', 'title': 'Gazdálkodási és menedzsment asszisztens', 'school': 'Pécsi Tudományegyetem · Közgazdaságtudományi Kar', 'date': '2020 — 2022', 'logo': 'pte.png',
     'topics': 'Vállalatirányítás · Gazdasági ismeretek · Menedzsment · Gyakorlati üzleti folyamatok'},
]
