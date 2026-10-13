def classify(value):
    if value < 148:
        return "Below range"
    elif 148 <= value <= 152:
        return "In range"
    else:
        return "Above range"

def calculate_average(total, count):
    average_snapshot = total / count
    average_result = average_snapshot
    return average_result

def main():
    num_bars = int(input("Enter the number of soap bars: "))
    
    total_weight = 0
    below_count = 0
    in_range_count = 0
    above_count = 0
    
    for _ in range(num_bars):
        weight = int(input("Enter the soap bar weight: "))
        classification = classify(weight)
        print(classification)
        
        total_weight += weight
        
        if classification == "Below range":
            below_count += 1
        elif classification == "In range":
            in_range_count += 1
        else:
            above_count += 1
            
    avg_weight = calculate_average(total_weight, num_bars)
    
    print(f"Total weight: {total_weight} g")
    print(f"Average weight: {avg_weight} g")
    print(f"Below range: {below_count}")
    print(f"In range: {in_range_count}")
    print(f"Above range: {above_count}")

if __name__ == "__main__":
    main()
