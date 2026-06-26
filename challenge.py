
# ================================================
# Hôpital District Kinkala
# ================================================
budget_kinkala = 12500000
consultation_kinkala = 1847
hospitalisation_kinkala = 312
Deces_hosp = 8
lits_totaux = 45
lits_occupes = 41
medecins_permanents = 3
pop_desservie = 85000

# ================================================
# CMS de Vindza
# ================================================
budget_vindza = 6800000
consultation_vindza = 923
hospitalisation_vindza = 87
Deces_hosp_vindza = 2
lits_totaux_vindza = 20
lits_occupes_vindza = 14
madecins_permanents_vindza = 1
pop_desservie_vindza = 42000

# ===============================================
# Hôpital de Kindamba
# ===============================================
budget_kindamba = 9200000
consultation_kindamba = 1234
hospitalisation_kindamba = 201
Deces_hosp_kindamba = 11
lits_totaux_kindamba = 35
lits_occupes_kindamba = 33
madecins_permanents_kindamba = 2
pop_desservie_kindamba = 67000

# ==============================================
# Calculs
# ==============================================
# Coût moyen par patient
cout_kinkala = budget_kinkala/consultation_kinkala
cout_vindza = budget_vindza/consultation_vindza
cout_kindamba = budget_kindamba/consultation_kindamba
# Taux d'occupation
occupation_kinkala = (lits_occupes/lits_totaux)*100
occupation_vindza = (lits_occupes_vindza/lits_totaux_vindza)*100
occupation_kindamba = (lits_occupes_kindamba/lits_totaux_kindamba)*100
# Densité médicale
densite_kinkala = (medecins_permanents/pop_desservie)*1000
densite_vindza = (madecins_permanents_vindza/pop_desservie_vindza)*1000
densite_kindamba = (madecins_permanents_vindza/pop_desservie_vindza)*1000
# Taux de mortalité
mortalite_kinkala = (Deces_hosp/hospitalisation_kinkala)*100
mortalite_vindza = (Deces_hosp_vindza/hospitalisation_vindza)*100
mortalite_kindamba = (Deces_hosp_kindamba/hospitalisation_kindamba)*100

print(f""" =====================================================
            RAPPORT
            =====================================================
            Coût moyen par patient kinkala : round({cout_kinkala},2) FCFA
            Taux d'occupation kinkala : round({occupation_kinkala},2)%
            Densité médicale kinkala : round({densite_kinkala},2) pour mille
            Taux de mortalité kinkala : round({mortalite_kinkala},2)%
            
            Coût moyen par patient vindza : round({cout_vindza},2) FCFA
            Taux d'occupation vindza : round({occupation_vindza},2)%
            Densité médicale vindza : round({densite_vindza},2) pour mille
            Taux de mortalité vindza : round({mortalite_vindza},2)%
      
            Coût moyen par patient kindamba : round({cout_kindamba},2) FCFA
            Taux d'occupation kindamba = round({occupation_kindamba},2)%
            Densité médicale kindamba = round({densite_kindamba},2) pour mille
            Taux de mortalité kindamba = round({mortalite_kindamba},2)%
      """)