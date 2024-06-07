replacements = {
    "dim_bc_balcony_01d" : "ex_common_balcony_01",
    "dim_bc_dormS_d" : "ex_common_dormer_square",
    "dim_bc_house_addon" : "ex_common_house_addon",
    "dim_bc_house_tall01dp" : "ex_common_house_tall_01",
    "dim_bc_house_tall02dp" : "ex_common_house_tall_02",
    "dim_bc_in_tower_th1dp" : "in_common_tower_thatch",
    "dim_bc_nord_house01" : "ex_nord_house_01",
    "dim_bc_nord_house02" : "ex_nord_house_02",
    "dim_bc_nord_house03" : "ex_nord_house_03",
    "dim_bc_nord_in_01" : "in_nord_house_02",
    "dim_bc_nord_in_02" : "in_nord_house_02",
    "dim_bc_nord_in_03" : "in_nord_house_03",
    "dim_bc_nord_win_com" : "ex_nord_win_01",
    "dim_bc_nord_win_com2" : "ex_nord_win_02",
    "dim_bc_pPkEndSideR" : "AB_In_ComPlainPkEndSideR",
    "dim_bc_pPkEntCornL" : "AB_In_ComPlainPkEntCornL",
    "dim_bc_skywalk_d" : "ex_common_skywalk_01",
    "dim_bc_tower_th_dp" : "ex_common_tower_thatch",
    "dim_bc_well" : "ex_nord_well_01",
}

reference_not_object_identifier = "\",\n        "

def replace_all(text, dict):
    for source, replacement in dict.items():
        if (source + reference_not_object_identifier) in text:
            print("Replacing " + source + " with " + replacement)
        text = text.replace(source  + reference_not_object_identifier, replacement  + reference_not_object_identifier)
    return text

with open('SNDLS.json', 'r') as input:
    content = input.read()

output_content = replace_all(content, replacements)

with open('SNDLS_unshabby.json', 'w+') as output:
    output.write(output_content)