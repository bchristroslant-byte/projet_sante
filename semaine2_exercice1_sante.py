
nom = "MAVOUNGOU Celestine"
age = 42
sexe = "F"
departement = "Brazzaville"
couverture = "CNS"

consultation = "Urgences"
cout_unitaire = 15000.0
nb_consultations = 1
remise_cnss = 0.3
diagnostic_principal = "Paludisme grave"

nom_hopital = "CHU de Brazzaville"
ville_hopital = "Brazzaville"
nb_lit_total = 320
nb_lit_occupes = 284
nb_medecins_actifs = 47

cout_total = (nb_consultations*cout_unitaire*remise_cnss)
taux_occupation = round((nb_lit_occupes/nb_lit_total)*100,1)

print(f"""=====================================================
          FICHE PATIENT - {nom}
          =====================================================
          Age            :{age}
          Sexe           :{sexe}
          Departement    :{departement}
          Couverture     :{couverture}
          -----------------------------------------------------
          CONSULTATION
          Type           :{consultation}
          Diagnostic     :{diagnostic_principal}
          Coût unitaire  :{cout_unitaire} FCFA
          Remise CNSS    :{remise_cnss*100}%
          Coût total     :{cout_total} FCFA
          -----------------------------------------------------
          HOPITAL : {nom_hopital}
          Ville          :{ville_hopital}
          Lits occupes   :{nb_lit_occupes} / {nb_lit_total} ({taux_occupation}%)
          Medecins actifs:{nb_medecins_actifs}
          Ratio consult  : 2.6 consultations / medecin ce matin
          =====================================================
          STATUT : Prise en charge validee
          =====================================================

""")


