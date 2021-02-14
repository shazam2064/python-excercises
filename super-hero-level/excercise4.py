# Cell styles
# Setting the font properties for a cell
'''All the available font-related options:
font = Font(name='Calibri',
            size=11,
            bold=False,
            italic=False,
            vertAlign=None,
            underline='none',
            strike=False,
            color='FF000000')

Source: https://openpyxl.readthedocs.io/en/stable/styles.html
'''
from openpyxl.styles import *

font = Font(color=colors.RED, bold=True, italic=True)

cell.font = font

# Setting the pattern/color properties for the cell
'''
fill = PatternFill(fill_type=None,
                   start_color='FFFFFFFF',
                   end_color='FF000000',
                   bgColor = 'FF000000',
                   fgColor = 'FF000000')

Source: https://openpyxl.readthedocs.io/en/stable/styles.html 
'''
from openpyxl.styles import *

fill = PatternFill(fill_type='solid', bgColor='F7FE2E')

cell.fill = fill

# Setting the border properties for the cell
'''
border = Border(left=Side(border_style=None, color='FF000000'),
                right=Side(border_style=None, color='FF000000'),
                top=Side(border_style=None,color='FF000000'),
                bottom=Side(border_style=None, color='FF000000'),
                diagonal=Side(border_style=None, color='FF000000'),
                diagonal_direction=0,
                outline=Side(border_style=None, color='FF000000'),
                vertical=Side(border_style=None, color='FF000000'),
                horizontal=Side(border_style=None, color='FF000000'))

Source: https://openpyxl.readthedocs.io/en/stable/styles.html 
'''
from openpyxl.styles import *

border = Border(left=Side(border_style='double', color='322FEC'), right=Side(border_style='double', color='322FEC'),
                top=Side(border_style='double', color='322FEC'), bottom=Side(border_style='double', color='322FEC'))

cell.border = border

# Setting the alignment properties for the cell
'''
alignment = Alignment(horizontal='general',
                    vertical='bottom',
                    text_rotation=0,
                    wrap_text=False,
                    shrink_to_fit=False,
                    indent=0)

Source: https://openpyxl.readthedocs.io/en/stable/styles.html 
'''
from openpyxl.styles import *

align = Alignment(horizontal='left')

cell.alignment = align