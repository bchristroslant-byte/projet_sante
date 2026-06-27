
# Taux de change
fcfa_euro = 656.957
fcfa_usd = 600.0
# Seuils OMS
seuil_densite = 0.05
seuil_mortalite = 2
# Département du Congo
departement = ["Brazzaville",
               "Pointe-Noire",
               "Kouilou",
               "Lekoumou",
               "Niari",
               "Bouenza",
               "Pool",
               "Plateaux",
               "Cuvette",
               "Cuvette ouest"
               "Sangha"
               "Likouala"
]
# Variables hôpitaux
chu_brazzaville = {
    "budget": 200000000,
    "medecin": 120,
    "lits": 500,
    "population": 2200000
}
hopital_pnr = {
    "budget": 100000000,
    "medecin": 80,
    "lits": 350,
    "population": 1200000
}
hopital_dolisie ={
    "budget": 4800000,
    "medecin": 25,
    "lits": 200,
    "population": 400000
}
hopital_owando = {
    "budget": 3800000,
    "medecin": 20,
    "lits": 150,
    "population": 400000
}
hopital_impfondo = {
    "budget": 2500000,
    "medecin": 10,
    "lits": 80,
    "population": 120000
}
#Variables médicaments
artemether_lume = {
    "quantite": 300,
    "rupture": 50,
    "prix": 3500
}
amoxiciline = {
    "quantite": 500,
    "rupture": 80,
    "prix": 1200
}
paracetamol = {
    "quantite": 1000,
    "rupture": 200,
    "prix": 300
}
sro = {
    "quantite": 450,
    "rupture": 60,
    "prix": 500
}
vaccin_antipalu = {
    "quantite": 250,
    "rupture": 30,
    "prix": 8500
}

# Calculs d'initialisation
total_medecins = (
    chu_brazzaville["medecin"]+
    hopital_dolisie["medecin"]+
    hopital_impfondo["medecin"]+
    hopital_owando["medecin"]+
    hopital_pnr["medecin"]
)
total_population = (
    chu_brazzaville["population"]+
    hopital_dolisie["population"]+
    hopital_impfondo["population"]+
    hopital_owando["population"]+
    hopital_pnr["population"]
)
densite_nat_medi = round((total_medecins/total_population)*1000,2)
stock_medicament = (
    artemether_lume["quantite"]+
    amoxiciline["quantite"]+
    paracetamol["quantite"]+
    sro["quantite"]+
    vaccin_antipalu["quantite"]
)

print(f"""
      Rapport d'inventaire
 ========== Section A : CONSTANTES NATIONALES Et NORMES OMS ======
        Taux_Euro_FCFA = {fcfa_euro}
        Taux_Euro_USD  = {fcfa_usd}
        Seuil_OMS_densite_medicale = 2.3 # medecins pour 1000 habitants
        Seuil_OMS_Vaccin = 95.0 # Pourcentage minimum OMS
        Seuil_Mortalite_alerte = 2.0  # deces/hospitalisations
        Seuil_rupture_stock_jours = 30 # jours minimun de stock
        Departement du Congo = {departement}
 
 ========= Section B : VARIABLES DES 5 HOPITAUX =============
        Hopital 1 = {chu_brazzaville}
        Ville     = {departement}
        Departement = {departement}
        Type        = CHU
        nb_de_lits = {chu_brazzaville['lits']}
        nb_de_medecins = {chu_brazzaville['medecin']}
        nb_de_occupes = 284
        nb_infirmiers = 123
        Population zone = {chu_brazzaville['population']}
========= Section C : VARIABLES DES 5 MEDICAMENTS ==========
       Medicament 1 = {artemether_lume}
       Medicament 2 = {paracetamol}
       Medicament 3 = {vaccin_antipalu}
       Medicament 4 = {sro}
       Medicament 5 = {amoxiciline}

========= Section D : CALCULS D'INITIALISATION ==============
        Densite medicale nationale = {densite_nat_medi}
        Stock de medicaments = {stock_medicament}
""")