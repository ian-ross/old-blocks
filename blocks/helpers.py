from datetime import datetime, date

from django.utils import timezone


class Week:
    def __init__(self, ts=None):
        if ts is None:
            ts = timezone.now()
        iso = ts.date().isocalendar()
        self.week = iso.week
        self.year = iso.year

    def start(self):
        return timezone.make_aware(datetime.fromisocalendar(self.year, self.week, 1))

    def end(self):
        return timezone.make_aware(datetime.fromisocalendar(self.year, self.week + 1, 1))


def project_grid_data(project, blocks):
    # Use project nominal total number of blocks and rows to calculate
    # grid columns.
    total = project.baseline + project.bonus
    rows = project.rows
    columns = total // rows + (1 if total % rows != 0 else 0)

    # Recalculate total and grid row count based on actual number of
    # blocks if there are more blocks than the project's nominal
    # total.
    total = max(total, len(blocks))
    rows = total // columns + (1 if total % columns != 0 else 0)

    # Partition blocks into those inside and outside current grid
    # bounds (to deal with case where grid has been reduced in size).
    inside, outside = [], []
    for b in blocks:
        if b.row < rows and b.column < columns:
            inside.append(b)
        else:
            outside.append(b)

    # Put the inside blocks into their cells.
    cells = {}
    for b in inside:
        cells[(b.row, b.column)] = b

    # Fit the outside blocks into empty cells in row, column order.
    outside.reverse()
    for r in range(rows):
        for c in range(columns):
            if len(outside) == 0:
                break
            if (r, c) in cells:
                continue
            cells[(r, c)] = outside.pop()

    # Blocks in row-major order.
    page_blocks = []
    for r in range(rows):
        for c in range(columns):
            if r * columns + c >= total:
                break
            
            # Baseline cells to left.
            page_block = {
                'row': r,
                'column': c,
                'baseline': c * rows + r < project.baseline
            }

            # Day for block colour.
            if (r, c) in cells:
                page_block['id'] = cells[(r, c)].pk
                page_block['day'] = f'day-{cells[(r, c)].start.isoweekday()}'

            page_blocks.append(page_block)
        
    return {
        'name': project.name,
        'id': project.pk,
        'rows': rows,
        'columns': columns,
        'page_blocks': page_blocks
    }


def project_next_cell(project, blocks):
    # Use project nominal total number of blocks and rows to calculate
    # grid columns.
    total = project.baseline + project.bonus
    rows = project.rows
    columns = total // rows + (1 if total % rows != 0 else 0)

    # Recalculate total and grid row count based on actual number of
    # blocks if there are more blocks than the project's nominal
    # total.
    total = max(total, len(blocks))
    rows = total // columns + (1 if total % columns != 0 else 0)

    # Find day of week.
    today = date.today().weekday()

    if rows >= 5 and today <= rows:
        # Try to find an empty cell in this today's row if we have
        # something like daily rows.
        for column in range(columns):
            if (today, column) not in blocks:
                return today, column

    # Otherwise just find the first empty cell.
    for row in range(rows):
        for column in range(columns):
            if (row, column) not in blocks:
                return row, column

    # And if that doesn't work, start a new row.
    return rows, 0
