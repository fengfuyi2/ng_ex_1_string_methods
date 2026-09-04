encoded = """
   !!junk-77!! | [3::DW::ok] | [xx::DRSC::bad] |
   [1::NFFU::ok] | ##nothing## | [5::TQI_QNGWFWD::ok] |
   [2::OG::ok] | [4::XLI::ok] | [7::WT7::bad] |
   [6::GZ_7_VS::ok] | [99::IGNORE_ME::bad] | %%noise%%
"""

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

encoded = encoded.replace("\n", "").replace("   ", " ").strip()
parts = encoded.split(" | ")

fragment_1 = ""
fragment_2 = ""
fragment_3 = ""
fragment_4 = ""
fragment_5 = ""
fragment_6 = ""
fragment_7 = ""

for part in parts:
    if part.startswith("[") and part.endswith("]"):
        inside = part[1:-1]
        segments = inside.split("::")
        number_str = segments[0]
        jumbled = segments[1]
        status = segments[2]

        if status == "ok":
            number = int(number_str)
            decoded = ""

            for char in jumbled:
                if char in alphabet:
                    pos = alphabet.find(char)
                    new_pos = pos - number
                    if new_pos < 0:
                        new_pos = new_pos + 26
                    decoded = decoded + alphabet[new_pos]
                else:
                    decoded = decoded + char

            if number_str == "1":
                fragment_1 = decoded
            elif number_str == "2":
                fragment_2 = decoded
            elif number_str == "3":
                fragment_3 = decoded
            elif number_str == "4":
                fragment_4 = decoded
            elif number_str == "5":
                fragment_5 = decoded
            elif number_str == "6":
                fragment_6 = decoded
            elif number_str == "7":
                fragment_7 = decoded

final_message = fragment_1 + " " + fragment_2 + " " + fragment_3 + " " + fragment_4 + " " + fragment_5 + " " + fragment_6 + " " + fragment_7
print(final_message)