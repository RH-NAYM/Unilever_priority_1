"""
Important Notes:
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


"""


convertionData = {
                    'GLOW & LOVELY BLMS BALM FOUNDATN CRM 40G': 'gl_foundation_crm',
                    'GLOW & LOVELY FACIAL MOIST ARYUVEDIC 50G': 'gl_aryuvedic_crm',
                    'GLOW & LOVELY FACIAL MST MLTVIT CRM 100G': 'gl_mltvit_crm',
                    'GLOW & LOVELY FACIAL MST MLTVIT CRM 50G': 'gl_mltvit_crm',
                    'PONDS FM CREAM COL MGT WHT BEAUTY 35G LC': 'ponds_white_beauty_crm',
                    'PONDS FM CRM COLMGT WHT BEAUTY SPTLS 25G': 'ponds_white_beauty_crm',
                    'GLOW & LOVELY FC WASH FM INSTA GLOW 100G': 'gl_insta_glow_fw',
                    'PONDS FWL ESSTNL CARE WHITE BEAUTY 100G': 'ponds_white_beauty_fw',
                    'PONDS FW LTN ESSNTL CARE PURE WHITE 100G': 'ponds_pure_white_fw',
                    'PONDS FW OIL CNTRL 100G': 'ponds_oil_control_fw',
                    'PONDS FWL CMGT PURE WHT CLAY FOAM 90G': 'ponds_pure_white_clay_fw',
                    'PONDS FWL CMGT WHT BEAUTY CLAY FOAM 90G': 'ponds_white_beauty_clay_fw',
                    'SUNSILK SHAMPOO BLACK 450ML': 'sunsilk_black_large',
                    'SUNSILK SHAMPOO BLACK 375ML': 'sunsilk_black_small',
                    'SUNSILK SHAMPOO BLACK 180ML': 'sunsilk_black_small',
                    'SUNSILK SHAMPOO THICK & LONG 450ML': 'sunsilk_tl_large',
                    'SUNSILK SHAMPOO THICK & LONG 375ML': 'sunsilk_tl_small',
                    'SUNSILK SHAMPOO THICK & LONG 180ML': 'sunsilk_tl_small',
                    'SUNSILK SHAMPOO HIJAB RCHRG REFRSH 375ML': 'sunsilk_hrr',
                    'SUNSILK SHMP HIJAB RECHRGE REFRESH 180ML': 'sunsilk_hrr',
                    'SUNSILK SHAMPOO VOLUME 375ML': 'sunsilk_volume',
                    'SUNSILK SHAMPOO VOLUME 195ML': 'sunsilk_volume',
                    'SUNSILK SHAMPOO FRESHNESS 375ML': 'sunsilk_fresh',
                    'SUNSILK SHAMPOO FRESHNESS 195ML': 'sunsilk_fresh',
                    'CLEAR SHAMPOO ANTI HAIR FALL 350ML': 'clear_ahf',
                    'CLEAR SHAMPOO ANTI HAIR FALL 180ML': 'clear_ahf',
                    'CLEAR SHAMPOO COMPLETE ACTVE CARE 350ML': 'clear_cac',
                    'CLEAR SHAMPOO COMPLETE ACTVE CARE 180ML': 'clear_cac',
                    'CLEAR MALE SHAMPOO CSM 450ML': 'clear_csm_large',
                    'CLEAR MALE SHAMPOO CSM 330ML': 'clear_csm_small',
                    'CLEAR MALE SHAMPOO CSM 180ML': 'clear_csm_small',
                    'TRESEMME SHAMPOO COLOR REVITALISE 580ML': 'tresemme_cr',
                    'TRESEMME SHAMPOO KERATIN SMOOTH 580ML': 'tresemme_ks_large',
                    'TRESEMME SHAMPOO KERATIN SMOOTH 340ML': 'tresemme_ks_small',
                    'DOVE SHAMPOO HAIR FALL RESCUE 650ML': 'dove_hfr_large',
                    'DOVE SHAMPOO HAIR FALL RESCUE 340ML': 'dove_hfr_small',
                    'DOVE SHAMPOO HAIR FALL RESCUE 170ML': 'dove_hfr_small',
                    'DOVE SHAMPOO IRP 650ML': 'dove_irp_large',
                    'DOVE SHAMPOO INTENSIVE REPAIR 340ML': 'dove_irp_small',
                    'DOVE SHAMPOO INTENSIVE REPAIR 170ML': 'dove_irp_small',
                    'DOVE HEALTHY GROWTH 340ML': 'dove_hg',
                    'DOVE SHAMPOO NOURISHING OIL 340ML': 'dove_no',
                    'DOVE HAIR RINSE OUT CONDITIONR HFR 180ML': 'dove_cond',
                    'DOVE REG RINSE OUT CNDTNR IRP 175ML': 'dove_cond',
                    'SUNSILK SHAMPOO HFS 375ML': 'sunsilk_hfs',
                    'SUNSILK SHAMPOO HFS 180ML': 'sunsilk_hfs',
                    'HORLICKS HFD STD JAR 1000G': 'horlicks_std',
                    'HORLICKS HFD STD JAR 500G': 'horlicks_std',
                    'HORLICKS HFD JUNIOR STAGE-2 JAR 500G': 'horlicks_junior',
                    'HORLICKS HFD CHOCOLATE JAR 500G': 'horlicks_choco',
                    'HORLICKS HFD WOMEN JAR 400G': 'horlicks_women',
                    'HORLICKS HFD MOTHER BIB 350G': 'horlicks_mother',
                    'HORLICKS HFD LITE JAR 330G': 'horlicks_lite',
                    'MALTOVA HFD STANDARD BIB 400G': 'maltova_std',
                    'BOOST HFD STANDARD JAR 400G': 'boost_std',
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
