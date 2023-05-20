from django.shortcuts import render

# TODO uwzględnić w widokach:
#     1. check-in pielgrzyma (admin - dostęp per albergue),
#     2. check-out pielgrzyma (admin - dostęp per albergue),
#     3. rezerwacja miejsc w albergue,
#     4. odwołanie rezerwacji
#     5. automatyczne wygasanie rezerwacji o jakiejś godzinie
#     6. informacja o obłożeniu danej albergue,
#     7. informacja o dodatkowych udogodnieniach,
#     8. zamówienie dodatkowych usług,
#     9. lista pielgrzymów w danym albergue danego dnia (admin - dostęp per albergue),
#     10. wyświetlenie etapów każdej z tras,
#     11. wyświetlenie dostępnych albergue na każdym etapie trasy
#  self-service:
#     TRASA -> ETAPY -> MIEJSCOWOŚCI -> ALBERGUE W DANEJ MIEJSCOWOŚCI -> INFO O OBŁOŻENIU ALBERGUE -> REZERWACJA/ODWOŁANIE REZERWACJI -> ZAMÓWIENIE DODATKOWYCH USŁUG
#  admin:
#     CHECK-IN -> CHECK-OUT -> LISTA PIELGRZYMÓW W ALBERGUE DANEGO DNIA
