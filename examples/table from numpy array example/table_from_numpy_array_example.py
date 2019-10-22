from python2latex import Document, Table, build
import numpy as np

doc = Document(filename='table_from_numpy_array_example', filepath='examples/table from numpy array example', doc_type='article', options=('12pt',))

sec = doc.new_section('Testing tables from numpy array')
sec.add_text("This section tests tables from numpy array.")

col, row = 6, 4
data = np.random.rand(row, col)

table = sec.new(Table(shape=(row+2, col+1), alignment='c', float_format='.2f'))
# Set a caption if desired
table.caption = 'Table from numpy array'
# Set entries with a slice directly from a numpy array!
table[2:,1:] = data

# Set a columns title as a multicell with custom parameters
table[0,1:4].multicell('Title1', h_align='c')
table[0,4:].multicell('Title2', h_align='c')
# Set subtitles as easily
table[1,1:] = [f'Col{i+1}' for i in range(col)]
# Set a subtitle on two lines if it is too long
table[1,-1:].divide_cell(shape=(2,1), alignment='c')[:] = [['Longer'],['Title']]

# Or simply create a new subtable as an entry
subtable = Table(shape=(2,1), as_float_env=False, bottom_rule=False, top_rule=False)
subtable[:,0] = ['From', 'Numpy']

# Chain multiple methods on the same area for easy combinations of operations
table[2:,0].multicell(subtable, v_align='*', v_shift='0pt').highlight('italic')
# Set multicell areas with a slice too
table[3:5,2:4] = 'Array' # The value is stored in the top left cell (here it would be cell (2,2))

# Add rules where you want, as you want
table[1,1:4].add_rule(trim_left=True, trim_right='.3em')
table[1,4:].add_rule(trim_left='.3em', trim_right=True)

# Automatically highlight the best value(s) inside the specified slice, ignoring text
for row in range(2,6):
    table[row,4:].highlight_best('low', 'italic') # Best per row, for the last 3 columns
# Highlights equal or near equal values too!
table[5,1] = 1.0
table[5,2] = 0.996
table[5].highlight_best('high', 'bold') # Whole row 4

tex = doc.build()
print(tex)
