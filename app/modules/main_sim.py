from dateutil import rrule
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.crud import crud
from app.modules.initialize import (
    start_date,
    end_date,
    trains,
    terminals
)
from app.modules.simulation import (
    simulate_terminal,
    simulate_export,
    simulate_train
)


async def main_func(
        calc_id: int,
        recalc: bool,
        session: AsyncSession
        ):
    for single_date in rrule.rrule(
        rrule.HOURLY,
        dtstart=start_date,
        until=end_date
    ):
        for terminal in terminals:
            simulate_terminal(terminal)
        for train in trains:
            if train.type == 'transport':
                simulate_train(train)
            else:
                simulate_export(train)
        for terminal in terminals:
            if recalc is False or recalc is None:
                await crud.post_to_db(
                    terminal,
                    single_date,
                    calc_id,
                    session)
            else:
                await crud.update_data(
                    terminal,
                    single_date,
                    calc_id,
                    session
                    )
        print(single_date)
