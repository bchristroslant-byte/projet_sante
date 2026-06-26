
budget_fcfa = 87450000
nb_consultation_ext = 4823
nb_hospitalisations = 1247
nb_deces = 18
nb_lits_total = 180
nb_lits_occupes = 143
nb_medecins = 22
nb_infirmiers = 58
population_dpt = 128000
taux_eur_fcfa = 655.957
taux_usd_fcfa = 600.0

budget_eur = budget_fcfa*taux_eur_fcfa
budget_usd = budget_fcfa*taux_usd_fcfa
densite_medicale = (nb_medecins/population_dpt)*1000
taux_mortalite = (nb_deces/nb_hospitalisations)*100
taux_occ_lits = (nb_lits_occupes/nb_lits_total)*100
budget_medicament = budget_fcfa*0.35
cout_journalier = 450000
jours_stock = budget_medicament//cout_journalier
jours_restants = budget_medicament%cout_journalier
budget_n_plus_1 = budget_fcfa*(1.08**2)

print(f"""
        === RAPPORT TRIMESTRIEL Q4 2025 - Hopital General Pointe-Noire ===
           BUDGET
             Depenses Q4     : {budget_fcfa} FCFA
             En euros        : {budget_eur}  EURO
             En dollars      : {budget_usd}  USD
           INDICATEURS OMS
            Densite medicale : 0.2 medecins / 1000 hab [Nomre OMS : sup=2.3]
            Taux mortalite   : {taux_mortalite} %
            Taux occupation  : {taux_occ_lits} %
           ANALYSE PHARMACIE
            Budget medicaments: {budget_medicament}
            Jours de stock    : {jours_stock} jours
            Jours depassement : {jours_restants} jours
           PROJECTION
           Budget N+2 (8%/an) : {budget_n_plus_1} FCFA
           ALERTE : Densite medicale critique (0.2 pour 1000 hab - norme OMS : 2.3)
""")     

