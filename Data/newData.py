"""
Important Notes:
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""


convertionData = {
                    'GAL BLM BBF CRM 40ML': 'gl_foundation_crm',
                    'GAL AV CRM 50ML': 'gl_aryuvedic_crm',
                    'GAL MV CRM 100ML /50ML/25ML': 'gl_mltvit_crm',
                    'PONDS WB CRM 35ML/ 25ML': 'ponds_white_beauty_crm',
                    'GAL FW 100ML': 'gl_insta_glow_fw',
                    'PONDS WB FW 100ML': 'ponds_white_beauty_fw',
                    'PONDS PURE WHT FW 100ML': 'ponds_pure_white_fw',
                    'PONDS FW OIL CNTRL 100ML': 'ponds_oil_control_fw',
                    'PONDS FWL CMGT PURE WHT CLAY FOAM 90G': 'ponds_pure_white_clay_fw',
                    'PONDS FWL CMGT WHT BEAUTY CLAY FOAM 90G': 'ponds_white_beauty_clay_fw',
                    'SS SHMP BLACK 450ML': 'sunsilk_black_large',
                    'SS SHMP BLACK 375ML/180ML': 'sunsilk_black_small',
                    'SS SHMP T&L 450ML': 'sunsilk_tl_large',
                    'SS SHMP T&L 375ML/180ML': 'sunsilk_tl_small',
                    'SUNSILK SHAMPOO HIJAB RCHRG REFRSH 375ML': 'sunsilk_hrr',
                    'SUNSILK SHMP HIJAB RECHRGE REFRESH 180ML': 'sunsilk_hrr',
                    'SS SHMP VOLUME 375ML/195ML': 'sunsilk_volume',
                    'SUNSILK SHAMPOO FRESHNESS 375ML': 'sunsilk_fresh',
                    'SUNSILK SHAMPOO FRESHNESS 195ML': 'sunsilk_fresh',
                    'CLEAR SHMP AHF 375ML/180ML': 'clear_ahf',
                    'CLEAR SHMP CAC 350ML/180ML': 'clear_cac',
                    'CLEAR MALE SHMP CSM 450ML': 'clear_csm_large',
                    'CLEAR MALE SHMP CSM 330ML/180ML': 'clear_csm_small',
                    'TRESEMME SHMP CR 580ML': 'tresemme_cr',
                    'TRESEMME SHMP KS 580ML': 'tresemme_ks_large',
                    'TRESEMME SHMP KS 340ML': 'tresemme_ks_small',
                    'DOVE SHMP HFR 650ML': 'dove_hfr_large',
                    'DOVE SHMP HFR 340ML/170ML': 'dove_hfr_small',
                    'DOVE SHMP IRP 650ML': 'dove_irp_large',
                    'DOVE SHMP IRP 340ML/170ML': 'dove_irp_small',
                    'DOVE HEALTHY GROWTH 340ML': 'dove_hg',
                    'DOVE SHMP NR OIL 340ML': 'dove_no',
                    'DOVE COND 180ML/175ML': 'dove_cond',
                    'SS SHMP HFS 375ML/180ML': 'sunsilk_hfs',
                    'HORLICKS STD JAR 1000G/500G': 'horlicks_std',
                    'HORLICKS JR STG JAR 500G': 'horlicks_junior',
                    'HORLICKS CHOC JAR 500G': 'horlicks_choco',
                    'HORLICKS WOMEN JAR 400G': 'horlicks_women',
                    'HORLICKS MOTHER BIB 350G': 'horlicks_mother',
                    'HORLICKS LITE JAR 330G': 'horlicks_lite',
                    'MALTOVA STANDARD BIB 400G': 'maltova_std',
                    'BOOST STD JAR 400G': 'boost_std',
                    'PEPSODENT SEN PROFESSIONAL': 'PEPSODENT',
                    'PEPSODENT ADV SEN FRESH': 'PEPSODENT',
                    'PEPSODENT SEN GUM CARE': 'PEPSODENT',
                    'VASELINE TM 200ML': 'vaseline_tm', 
                    'Vaseline Deep Restore hh':'vaseline_tm',
                    'Vaseline Deep Restore Lotion': 'vaseline_tm',
                    'Vaseline Daily Brightening Lotion': 'vaseline_hw',
                    'VASELINE HW 200ML': 'vaseline_hw',
                    'Vaseline Aloe Fresh Lotion': 'vaseline_aloe',
                    'VASELINE ALOE 200ML': 'vaseline_aloe',
                    'Dove Nourishing Body Care Lotion': 'dove_qpds',
                    'DOVE 250ML': 'dove_qpds',
                }

validation = [
                "da_skin_care_st",
                "da_hair_care_st",
                "da_oral_care_st",
                "da_nutrition_st",
                "qpds_st"
            ]
            
self_talker = {
                "Hair Care":"da_hairr_care_st",
                "Face Cream":"da_skin_care_st",
                "Face Wash":"da_skin_care_st",
                "NS Single Shelf":"da_nutrition_st",
                "NS Double Shelf":"da_nutrition_st",
                "NS Triple Shelf":"da_nutrition_st",
                "NS Drug Store":"da_nutrition_st",
                "QPDS Vaseline":"qpds_st",
                "QPDS Vaseline 1":"qpds_st"
            }

sos_convertion_data = {
                        "H&H":{
                                "Reckitt Benckser":["Harpic"]
                                },
                        "Nutrition":{
                                        "Abul Khair":["Marks"],
                                        "ARLA FOODs":["Dano"]
                                        },
                        "Oral":{
                                    "ACI":["Colgate"],
                                    "Anfords BD LTD":["Mediplus"],
                                    "Unilever":["CLOSE UP","PEPSODENT"]
                                    },
                        "Skin Care":{
                                        "Himalaya":["Himalaya"],
                                        "Unilever":["GLOW & LOVELY","PONDS"]
                                        },
                        "Skin Cleansing":{
                                            "Keya Cosmetic Ltd":["Keya"],
                                            "Kohinoor Chemical Ltd":["Bactrol","Sandalina","Tibet"],
                                            "Reckitt Benckser":["Dettol"],
                                            "Square Toiletries Ltd":["Meril"],
                                            "Unilever":["LIFEBUOY","LUX"]
                                            }
                       }
