import tkinter as tk
import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import networkx as nx
import pandas as pd
import webbrowser

# Event Construct ------------------------------------------------------------------------

root = ctk.CTk()
root.geometry("1000x700")

G = nx.Graph()


df = pd.read_csv("CSC 230_ Project - Names.csv", index_col=0)
df2 = pd.read_csv("CSC 230_ Project - Help.csv", index_col=0)
df3 = pd.read_csv("CSC 230_ Project - Outside.csv", index_col=0)


df['First Name'] = df.index.str.split().str[0]



# Event Construct ------------------------------------------------------------------------
# ========================================================================================
# Tabs -----------------------------------------------------------------------------------

tabview = ctk.CTkTabview(master=root)
tabview.pack(padx=00, pady=00)

tabview.add("tab 1")
tabview.add("tab 2")

# Tabs -----------------------------------------------------------------------------------
# ========================================================================================
# Defines --------------------------------------------------------------------------------

def button_callback(): #Button
    print("button clicked")
    url1 = "www.linkedin.com/in/ashovkatov"

    # Open the URL in the default web browser
    webbrowser.open_new(url1)


def draw_graph(): #Graph setting

    G.add_nodes_from(df.index)
    edge_widths={}

    for source, row in df.iterrows(): #1st CSV file setup
        for target, value in row.items():
            if pd.notnull(value) and value == 1:
                G.add_edge(source, target)
                edge_widths[(source, target)] = 2


    edge_colors = {}                  #2nd CSV file setup and let it make changes
    for source, row in df2.iterrows():
        for target, color_value in row.items():
            if pd.notnull(color_value):
                if pd.notnull(color_value) and color_value == 1:
                    if (source, target) in G.edges():
                        if nx.get_edge_attributes(G, 'color').get((source, target)) == 'red':
                            edge_colors[(source, target)] = 'blue'
                        else:
                            edge_colors[(source, target)] = 'orange'  # Know Name and Helped
                    else:
                        edge_colors[(source, target)] = 'green'

    edge_colors1 = {}                  #3rd CSV file setup and let it make changes
    for source, row in df3.iterrows():
        for target, color_value in row.items():
            if pd.notnull(color_value):
                if pd.notnull(color_value) and color_value == 1:
                    if (source, target) in G.edges():
                        if nx.get_edge_attributes(G, 'color').get((source, target)) == 'green':
                            edge_colors1[(source, target)] = 'yellow'
                        else:
                            edge_colors1[(source, target)] = 'purple'  # Know Name and Hanged out
                    else:
                        edge_colors1[(source, target)] = 'red'


    widths = [4 if color == 'orange' else (0.01 if color == 'black' else (0.5 if color == 'red' else (1.5 if color == 'green' else 10))) for color in edge_colors.values()]

    pos = nx.circular_layout(G)
    plt.figure(figsize=(14, 14))
    node_sizes = [200 * G.degree[node] for node in G.nodes()]
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=node_sizes, font_size=8)
    nx.draw_networkx_edges(G, pos, edgelist=edge_colors.keys(), edge_color=list(edge_colors.values()), width=widths)
    nx.draw_networkx_edges(G, pos, edgelist=edge_colors1.keys(), edge_color=list(edge_colors1.values()), width=widths)



    # Draw
    canvas = FigureCanvasTkAgg(plt.gcf(), master=tabview.tab("tab 1"))
    canvas.draw()
    canvas.get_tk_widget().pack()

def draw_graph1():
    df0 = pd.read_csv("CSC 230_ Project - Names.csv", index_col=0)
    df01 = pd.read_csv("CSC 230_ Project - Help.csv", index_col=0)
    G1 = nx.Graph()
    G1.add_nodes_from(df.index)

    for source, row in df0.iterrows():
        for target, value in row.items():
            if pd.notnull(value) and value == 1:
                G1.add_edge(source, target)

    edge_colors = {}
    for source, row in df01.iterrows():
        for target, value in row.items():
            if pd.notnull(value) and value == 1:
                edge_colors[(source, target)] = 'green'

    subgraph_edges = [("Akmal Shovkatov", target) for target in G1.neighbors("Akmal Shovkatov")]
    SG = G1.edge_subgraph(subgraph_edges)

    # Set
    pos1 = nx.spring_layout(SG)
    plt.figure(figsize=(8, 6))
    nx.draw(SG, pos1, with_labels=True, node_color='skyblue', node_size=4000)
    nx.draw_networkx_edges(SG, pos1, edge_color=[edge_colors.get(edge, 'grey') for edge in SG.edges], width=5)

    # Draw
    canvas = FigureCanvasTkAgg(plt.gcf(), master=tabview.tab("tab 2"))
    canvas.draw()
    canvas.get_tk_widget().pack()



# Defines --------------------------------------------------------------------------------



#label
label = ctk.CTkLabel(master=tabview.tab("tab 1"), text="Table for whole Group", font=("Arial",24), text_color="skyblue" )
label1 = ctk.CTkLabel(master=tabview.tab("tab 1"), text="Black #5 (name only)  |  Orange #2 (know name and helped  |  Purple #1 (know name and hanged out)", font=("Arial",18), text_color="white" )
label2 = ctk.CTkLabel(master=tabview.tab("tab 1"), text="Green #3 (Only Hanged out)  |  Red #4 (Don't know the Name )", font=("Arial",18), text_color="white")
label3 = ctk.CTkLabel(master=tabview.tab("tab 2"), text="Akmal Shovkatov's (me) personal table | Green (helped)", font=("Arial",20), text_color="white" )

label.pack()
label1.pack()
label2.pack()
label3.pack()

#draw button1
button = ctk.CTkButton(root, text="LinkedIn link", command=button_callback)
button.pack(padx=20, pady=20)

#draw graph1
draw_graph()

#draw graph2
draw_graph1()


root.mainloop()