import matplotlib.pyplot as plt

def group_data(categories, values):
    grouped_data = {}
    for cat, val in zip(categories, values):
        grouped_data[cat] = grouped_data.get(cat, 0) + val
    return grouped_data

def plot_grouped_data(grouped_data):
    plt.bar(grouped_data.keys(), grouped_data.values())
    plt.xlabel("Category")
    plt.ylabel("Total Value")
    plt.title("Grouped Data Bar Chart")
    plt.savefig("output.png")
    plt.close()

def main():
    categories = ["A", "B", "A", "C", "B", "A"]
    values = [10, 20, 15, 30, 25, 5]

    grouped = group_data(categories, values)
    print("Grouped Data:", grouped)

    plot_grouped_data(grouped)
    print("Graph saved as output.png")

if __name__ == "__main__":
    main()
