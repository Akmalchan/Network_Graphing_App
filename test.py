# import module
from matplotlib_venn import venn3, venn3_circles
from matplotlib import pyplot as plt

# depict venn diagram
v = venn3(subsets=(2500, 1300, 200, 200, 0, 0, 200),
          set_labels=('Names', 'Help', 'OutSide'),
          set_colors=("red", "cyan", "palegreen"), alpha=0.7)

# outline of circle line style and width
venn3_circles(subsets=(2500, 1300, 200, 200, 0, 0, 200),
              linestyle="solid", linewidth=.2)

# Your list of labels
labels = ['100', '101', '110', '010', '001', '011', '111']

# Your list of texts
texts = ["|An_Bn_C|\nBen\nAaron\nBrandy\nSteven\nAndrew\nDante\nDenis\nJacob\nLuca\nLucas\nMaxwell\nRandy\nShana\nTavasya\nVansh", "", "|AnBn_C|\nHayk\nRajvir\nKhang\nMisha\nSignora", "", "", "", ""]

# Loop through both lists simultaneously using zip
for label, text in zip(labels, texts):
    v.get_label_by_id(label).set_text(text)

plt.text(3, 0, ' ')
plt.text(.75, 0, '|_An_Bn_C|\nAdrian Murillo\nBen Riekes\nConnor Moore\nDavid L. Lei\nDavid U. Ung\nRay Guo\nLuca Valencia\nJeremy\nJuan Navarro\nJulia Whelan\nJustin Ho\nKrish Adya\nKyle Donaldson\nMichael A.\nMichael T.\nNaomi Lozano\nParth Bansal\nRyan George\nVishruta', fontsize=8, color='grey')

# title of the venn diagram
plt.title("Akmal the Great Venn Diagram")
plt.show()

