from datetime import datetime
from sqlalchemy import select
from sqlalchemy.orm import Session
import openpyxl

from app.core.terminal import Terminal
from app.core.train import Train
from app.db.db import SessionLocal, Base
from app.db.models.raduzhny import Raduzhny
from app.db.models.zvezda import Zvezda
from app.db.models.polarny import Polarny


class CRUD:

    def __init__(self):
        self.model_list = [Polarny, Raduzhny, Zvezda]

    def get(
            self,
            calc_id: int,
            session: Session
    ):
        res = []
        for model in self.model_list:
            print(model)
            obj = session.execute(select(model).where(
                model.calc_id == calc_id
            ))
            obj = obj.scalars().all()
            wb = openpyxl.Workbook()
            '''
            db_table_names = list(Base.metadata.tables.keys())
            for i in range(len(db_table_names)):
                wb.create_sheet(db_table_names[i], index=i)'''
            sheet = wb.active
            for j in range(1, 5):
                for k in range(1, 10):
                    cell = sheet.cell(row=j, column=k)
                    cell.value = obj[1].oil
            wb.save('C:\\Dev\\trains_and_oil\\app\\api\\get_db_data.xlsx')

        print(wb.sheetnames)
        return 

    def get_train_name(
            self,
            train: Train
    ):
        train_name = None
        if train is not None:
            train_name = train.name
        return train_name

    def crud_transshipment_point(
            self,
            terminal: Terminal,
            start_date: datetime,
            calc_id: int,
            session: Session
    ):
        new_obj = Polarny(
            datetime=start_date,
            oil=terminal.oil,
            train_name_1=self.get_train_name(terminal.ways.get(1)),
            train_1_unloading=terminal.unloading,
            train_name_2=self.get_train_name(terminal.ways.get(2)),
            train_2_unloading=terminal.unloading,
            train_name_3=self.get_train_name(terminal.ways.get(3)),
            train_3_unloading=terminal.unloading,
            calc_id=calc_id
        )
        session.add(new_obj)
        session.commit()
        return

    def crud_production_point(
            self,
            terminal: Terminal,
            start_date: datetime,
            calc_id: int,
            session: Session
    ):
        if terminal.name == 'raduzhny':
            new_obj = Raduzhny(
                datetime=start_date,
                oil=terminal.oil,
                train_name=self.get_train_name(terminal.ways.get(1)),
                train_unloading=terminal.unloading,
                calc_id=calc_id
            )
        else:
            new_obj = Zvezda(
                datetime=start_date,
                oil=terminal.oil,
                train_name=self.get_train_name(terminal.ways.get(1)),
                train_unloading=terminal.unloading,
                calc_id=calc_id
            )
        session.add(new_obj)
        session.commit()
        return

    def post_to_db(
        self,
        terminal: Terminal,
        start_date: datetime,
        calc_id: int,
        session: Session
    ):
        if terminal.type != 'transshipment_point':
            self.crud_production_point(
                terminal,
                start_date,
                calc_id,
                session
                )
        else:
            self.crud_transshipment_point(
                terminal,
                start_date,
                calc_id,
                session
                )
        return

    def update_data(
        self,
        terminal: Terminal,
        start_date: datetime,
        calc_id: int,
        session: Session
    ):
        for model in self.model_list:
            session.query(model).filter(
                model.calc_id == calc_id,
                model.datetime == start_date
            ).delete()
        session.commit()
        self.post_to_db(terminal, start_date, calc_id, session)
        return

    def delete_obj(
            self,
            calc_id: int,
            session: Session
    ):
        for model in self.model_list:
            session.query(model).filter(
                model.calc_id == calc_id
            ).delete()
        session.commit()
        return

    def delete_all(
            self,
            session: Session
            ):
        for model in self.model_list:
            session.query(model).delete()
        session.commit()
        return


crud = CRUD()
