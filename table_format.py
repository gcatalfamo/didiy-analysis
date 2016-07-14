import itable
 # functions to set styles
def _set_cell_style(self, style=None, tuples=None, rows=None, cols=None, format_function=None, **kwargs):
    if style is None:
        style = CellStyle()
    for key, value in kwargs.items():
        k = key.replace("_", "-")
        style.set(k, value)
    if format_function is not None:
        style.format_function = format_function
    if tuples:
        for tup in tuples:
            i = tup[0]
            j = tup[1]
            self.cell_styles[i][j] = style.copy()
    if rows is None and cols is None:
        return
    if rows is None:
        rows = range(self.num_rows)
    if cols is None:
        cols = range(self.num_cols)
    for i in rows:
        for j in cols:
            self.cell_styles[i][j] = style.copy()
def _set_row_header_style(self, style=None, indices=None, format_function=None, **kwargs):
    if style is None:
        style = CellStyle()
    for key, value in kwargs.items():
        k = key.replace("_", "-")
        style.set(k, value)
    if format_function is not None:
        style.format_function = format_function
    if indices is None:
        indices = range(self.num_rows)
    for i in indices:
        self.header_row_styles[i] = style.copy()

def _set_col_header_style(self, style=None, indices=None, format_function=None, **kwargs):
    if indices is None:
        indices = range(self.num_cols)
    if style is None:
        style = CellStyle()
    if format_function is not None:
        style.format_function = format_function
    for key, value in kwargs.items():
        k = key.replace("_", "-")
        style.set(k, value)
    for i in indices:
        self.header_col_styles[i] = style.copy()

itable.PrettyTable.set_cell_style = _set_cell_style
itable.PrettyTable.set_row_header_style = _set_row_header_style
itable.PrettyTable.set_col_header_style = _set_col_header_style
back_y = itable.CellStyle()
back_y.set("background-color", "yellow")
w = itable.CellStyle()
w.set("color", "white")
r = itable.CellStyle()
r.set("color", "red")
g = itable.CellStyle()
g.set("color", "green")
