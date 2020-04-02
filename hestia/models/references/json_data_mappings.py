from pathlib import Path

DATA_MAPPING = dict(
    location = Path('data'),
    constants= {
        # net heating values
        'Conv_Diesel_kg_kWh':'net_heating_diesel_kWh',
        'Conv_GWP_N2O':'gwp_n2o',
        'Conv_GWP_CH4':'gwp_ch4',
        'Conv_Fert_UAN_Urea': 'synth_fert_nutrient_urea_n',
        # atomic weights
        'Conv_Mol_N2ON_N2O':'c_n2on_n2o',
        'Conv_Mol_NO3N_NO3':'c_no3n_no3',
        'Conv_Mol_NH3N_NH3':'c_nh3n_nh3',
        'Conv_Mol_NON_NO':'c_non_no',
        # emission factors
        'EF_Dolomite_CO2':'co2_dolomite',
        'EF_Lime_CO2':'co2_lime',
        'EF_Urea_CO2':'co2_urea',
        'EF_Fert_High_NO3N':'c_leaching_no3_n_high',
        'EF_Fert_Low_NO3N':'c_leaching_no3_n_low',
        'EF_Fert_NO3N':'c_leaching_no3_n_other',
        'EF_Fert_FRice_NO3N':'c_leaching_no3_n_flooded_rice',
        'EF_FertExcr_Pasture_NO3N':'c_leaching_no3_n_pasture',
        'EF_Ind_NH3NNOxN_N2O':'c_nh3nnoxn_n2o',
        'EF_Ind_NO3N_N2O':'c_no3n_n2o',
        'EF_CRes_N_N2O':'n2o_residue_direct',
        'EF_Burn_DM_N2O':'n2o_residue_burn_direct',
        'EF_Burn_DM_NH3':'nh3_residue_burn_direct',
        'EF_Burn_DM_NOx':'nox_residue_burn_direct',
        'EF_Burn_DM_CH4':'ch4_residue_burn_direct',
        # loss factors
        'Frac_Vol_SynthN':'loss_factor_synt_n',
        'Frac_Vol_OrgN':'loss_factor_org_n',
        # Emissions from fuel
        'GHG_Inputs_Diesel':'ghg_disel_prod',
        'GHG_Field_Diesel':'ghg_disel_combustion',
        'Eutr_Inputs_Diesel':'eutr_disel_prod',
        'Acid_Inputs_Diesel':'acid_disel_prod',
        'Eutr_Field_Diesel':'eutr_disel_combustion',
        'Acid_Field_Diesel':'acid_disel_combustion',
        # Emissions from electricity
        'GHG_Electricity':'ghg_electricity',
        'Eutr_Electricity':'eutr_electricity',
        'Acid_Electricity':'acid_elecrtricity',
        # Emissions from machinery and infrastructure:
        # eutrophication
        'Eutr_Inputs_Machinery':'eutr_machinery',
        'Eutr_Inputs_Glass':'eutr_glass',
        'Eutr_Inputs_Plastic':'eutr_plastic',
        'Eutr_Inputs_RockWool':'eutr_rockwool',
        'Eutr_Inputs_Steel':'eutr_steel',
        'Eutr_Inputs_Aluminium':'eutr_aluminium',
        'Eutr_Inputs_Iron':'eutr_iron',
        'Eutr_Inputs_Concrete':'eutr_concrete',
        'Eutr_Inputs_Wood':'eutr_wood',
        # ghg
        'GHG_Inputs_Machinery': 'ghg_machinery',
        'GHG_Inputs_Glass': 'ghg_glass',
        'GHG_Inputs_Plastic': 'ghg_plastic',
        'GHG_Inputs_RockWool': 'ghg_rockwool',
        'GHG_Inputs_Steel': 'ghg_steel',
        'GHG_Inputs_Aluminium': 'ghg_aluminium',
        'GHG_Inputs_Iron': 'ghg_iron',
        'GHG_Inputs_Concrete': 'ghg_concrete',
        'GHG_Inputs_Wood': 'ghg_wood',
        # acidification
        'Acid_Inputs_Machinery': 'acid_machinery',
        'Acid_Inputs_Glass': 'acid_glass',
        'Acid_Inputs_Plastic': 'acid_plastic',
        'Acid_Inputs_RockWool': 'acid_rockwool',
        'Acid_Inputs_Steel': 'acid_steel',
        'Acid_Inputs_Aluminium': 'acid_aluminium',
        'Acid_Inputs_Iron': 'acid_iron',
        'Acid_Inputs_Concrete': 'acid_concrete',
        'Acid_Inputs_Wood': 'acid_wood',
        # Emissions from fertilizers production
        # ghg
        'GHG_Inputs_SynthN': 'ghg_from_synth_fert_avg',
        'GHG_Inputs_SynthPhos': 'ghg_from_synth_phos_avg',
        'GHG_Inputs_SynthPot': 'ghg_from_synth_pot_avg',
        'GHG_Inputs_Lime': 'ghg_from_lime_avg',
        'GHG_Inputs_Pesticide': 'ghg_from_pesticide_avg',
        # acidification
        'Acid_Inputs_SynthN': 'acid_from_synth_fert_avg',
        'Acid_Inputs_SynthPhos': 'acid_from_synth_phos_avg',
        'Acid_Inputs_SynthPot': 'acid_from_synth_pot_avg',
        'Acid_Inputs_Lime': 'acid_from_lime_avg',
        'Acid_Inputs_Pesticide': 'acid_from_pesticide_avg',
        # eutrophication
        'Eutr_Inputs_SynthN': 'eutr_from_synth_fert_avg',
        'Eutr_Inputs_SynthPhos': 'eutr_from_synth_phos_avg',
        'Eutr_Inputs_SynthPot': 'eutr_from_synth_pot_avg',
        'Eutr_Inputs_Lime': 'eutr_from_lime_avg',
        'Eutr_Inputs_Pesticide': 'eutr_from_pesticide_avg'
    },

    lists = {
        # Emissions from synthetic fertilizers
        'Table_GWP_Inputs_SynthN':'gwp_from_synth_fert',
        'Table_Acid_Inputs_SynthN':'acid_from_synth_fert',
        'Table_Eutr_Inputs_SynthN':'eutr_from_synth_fert',
        # Emissions from fertilizer use
        'List_NOx_Ctry_EF': 'nox_emiss_by_country',
        'Table_ExcrNH3_TAN_NH3': 'nh3_emiss_from_excreta_tan',
        'Table_ExcrNH3_Animal': 'nh3_emiss_from_excreta_sources',
        'Table_OrgFert_TAN_NH3': 'nh3_tan_from_org_fert',
        'Table_FertComp_Global':'synth_fert_use_global',
        'List_FAO_Countries':'fao_countries',
        'List_FAO_Countries_H': 'fao_countries_h',
        'List_Climate_N2ON':'climate_n2o_n',
        'List_Climate_NOxN':'climate_nox_n',
        'List_IPCC_Crops_N2ON':'ipcc_crops_n2o_n',
        'List_Climate_Zone':'climate_zone',
        'List_IPCC_Crops_H':'ipcc_crops',
        # crop residue
        #'List_CRes_Crops': 'res_from_dmyield_crops',
        'List_CRes_Names': 'residue_crop_names',
        'List_CRes_Slope': 'residue_slope',
        'List_CRes_Intercept': 'residue_intercept',
        'List_CRes_N_AG': 'residue_n_content_ag',
        'List_CRes_Ratio': 'residue_ratio_ag_to_bg',
        'List_CRes_N_BG': 'residue_n_content_bg',
        'List_CRes_CF': 'residue_combustion',
        'Table_CRes_Burnt': 'residue_burn_share',
        'Table_CRes_Rem': 'residue_removed_share',
        'Table_CRes_Crop': 'residue_share_crops',
        'Table_CRes_Ctry': 'residue_share_countries',
        # P emissions
        'List_C2Factors': 'p_loss_c2_till_factor',
        'List_C2Factors_Tillage': 'p_loss_c2_till',
        'List_C2Factors_Ctry': 'p_loss_c2_ctry_factor',
        'List_C1Factors_Crops': 'p_loss_c1_crop',
        'List_C1Factors': 'p_loss_c1_crop_factor',
        'Table_NH3_From_Synt_Acid_Soil':'nh3_synth_acid_soil',
        'Table_NH3_From_Synt_Alkaline_Soil':'nh3_synth_alk_soil',
        # P practice
        'Spatial_P_Practice':'p_practice_by_location',
        'Spatial_Lat_Lon':'p_practice_locations',
        # practice correction factors
        'List_PCorr': 'correction_for_practice_factor',
        'List_PCorr_Slope': 'correction_for_practice_factor_slope',
        # Electricity emissions
        'List_GWP_Electricity_Ctry':'gwp_from_elecrticity',
        'List_Eutr_Electricity_Ctry':'po4_from_elecrticity',
        'List_Acid_Electricity_Ctry': 'so2_from_electricity',
        'List_Electricity_Ctry':'electricity_emissions_countries'
    })
