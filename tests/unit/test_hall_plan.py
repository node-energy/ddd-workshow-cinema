import unittest
from src.domain.ticket_selling.models import HallPlan, Seat, SeatRow, Status


def create_hall_plan_with_rows_and_seats():
    rows: list[SeatRow] = []
    for i in range(1,10):
        seats: list[Seat] = []
        for j in range(1, 5):
            seats.append(Seat(number=j, status=Status.open))
        rows.append(SeatRow(number=i, seats=seats))
    return HallPlan(rows=rows)


class HallPlanTestCase(unittest.TestCase):
    def test_mark_as_sold(self):
        hall_plan = create_hall_plan_with_rows_and_seats()
        row_number = 2
        seat_number = 4
        hall_plan.mark_as_sold(row_number=row_number, seat_number=seat_number)
        row = next(r for r in hall_plan.rows if r.number == row_number)
        seat = next(s for s in row.seats if s.number == seat_number)
        self.assertEqual(
            seat.status, Status.reserved
        )


if __name__ == '__main__':
    unittest.main()
