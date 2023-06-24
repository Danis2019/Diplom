from sqlalchemy import MetaData, Table, Column, Integer, String

metadata = MetaData()

features = Table(
    "Features",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("direction_X", Integer, nullable=False),
    Column("direction_Y", Integer, nullable=False),
    Column("direction_wall", Integer, nullable=False),
    Column("target", Integer, nullable=False)
)
table_x = Table(
    "Name_direction_X",
    metadata,
    Column("direction_X", String, nullable=False),
    Column("Name", String, nullable=False),
)
table_y = Table(
    "Name_direction_Y",
    metadata,
    Column("direction_Y", String, nullable=False),
    Column("Name", String, nullable=False),
)
table_wall = Table(
    "Name_direction_Wall",
    metadata,
    Column("direction_Wall", String, nullable=False),
    Column("Name", String, nullable=False),
)