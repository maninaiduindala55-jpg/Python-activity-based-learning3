total_classes = int(input("Enter total classes conducted: "))
attended_classes = int(input("Enter classes attended: "))
required_percentage = float(input("Enter required attendance percentage: "))

if total_classes <= 0 or attended_classes < 0 or attended_classes > total_classes:
    print("Invalid attendance details")

elif required_percentage <= 0 or required_percentage > 100:
    print("Invalid required percentage")

else:
    current_percentage = (attended_classes / total_classes) * 100

    print("Current attendance:", round(current_percentage, 2), "%")

    if current_percentage >= required_percentage:
        additional_classes = 0
        print("Required attendance already achieved")

    else:
        additional_classes = 0

        while ((attended_classes + additional_classes) /(total_classes + additional_classes)) * 100 < required_percentage:additional_classes += 1

        print("Additional classes required:", additional_classes)