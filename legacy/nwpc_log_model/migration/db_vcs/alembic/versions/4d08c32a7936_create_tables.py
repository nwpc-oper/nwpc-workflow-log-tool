"""create tables

Revision ID: 4d08c32a7936
Revises: 
Create Date: 2017-09-18 08:14:04.575755

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d08c32a7936'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('record',
    sa.Column('repo_id', sa.Integer(), nullable=False),
    sa.Column('version_id', sa.Integer(), nullable=False),
    sa.Column('line_no', sa.Integer(), nullable=False),
    sa.Column('record_type', sa.String(length=100), nullable=True),
    sa.Column('record_date', sa.Date(), nullable=True),
    sa.Column('record_time', sa.Time(), nullable=True),
    sa.Column('record_command', sa.String(length=100), nullable=True),
    sa.Column('record_fullname', sa.String(length=200), nullable=True),
    sa.Column('record_additional_information', sa.Text(), nullable=True),
    sa.Column('record_string', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('repo_id', 'version_id', 'line_no')
    )
    op.create_table('record.nwp_pos.nwpc_sp',
    sa.Column('repo_id', sa.Integer(), nullable=False),
    sa.Column('version_id', sa.Integer(), nullable=False),
    sa.Column('line_no', sa.Integer(), nullable=False),
    sa.Column('record_type', sa.String(length=100), nullable=True),
    sa.Column('record_date', sa.Date(), nullable=True),
    sa.Column('record_time', sa.Time(), nullable=True),
    sa.Column('record_command', sa.String(length=100), nullable=True),
    sa.Column('record_fullname', sa.String(length=200), nullable=True),
    sa.Column('record_additional_information', sa.Text(), nullable=True),
    sa.Column('record_string', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('repo_id', 'version_id', 'line_no')
    )
    op.create_index('nwp_pos_nwpc_sp_command_index', 'record.nwp_pos.nwpc_sp', ['record_command'], unique=False)
    op.create_index('nwp_pos_nwpc_sp_date_time_index', 'record.nwp_pos.nwpc_sp', ['record_date', 'record_time'], unique=False)
    op.create_index('nwp_pos_nwpc_sp_fullname_index', 'record.nwp_pos.nwpc_sp', ['record_fullname'], unique=False)
    op.create_index('nwp_pos_nwpc_sp_type_index', 'record.nwp_pos.nwpc_sp', ['record_type'], unique=False)
    op.create_table('record.nwp_vfy.nwpc_vfy',
    sa.Column('repo_id', sa.Integer(), nullable=False),
    sa.Column('version_id', sa.Integer(), nullable=False),
    sa.Column('line_no', sa.Integer(), nullable=False),
    sa.Column('record_type', sa.String(length=100), nullable=True),
    sa.Column('record_date', sa.Date(), nullable=True),
    sa.Column('record_time', sa.Time(), nullable=True),
    sa.Column('record_command', sa.String(length=100), nullable=True),
    sa.Column('record_fullname', sa.String(length=200), nullable=True),
    sa.Column('record_additional_information', sa.Text(), nullable=True),
    sa.Column('record_string', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('repo_id', 'version_id', 'line_no')
    )
    op.create_index('nwp_vfy_nwpc_vfy_command_index', 'record.nwp_vfy.nwpc_vfy', ['record_command'], unique=False)
    op.create_index('nwp_vfy_nwpc_vfy_date_time_index', 'record.nwp_vfy.nwpc_vfy', ['record_date', 'record_time'], unique=False)
    op.create_index('nwp_vfy_nwpc_vfy_fullname_index', 'record.nwp_vfy.nwpc_vfy', ['record_fullname'], unique=False)
    op.create_index('nwp_vfy_nwpc_vfy_type_index', 'record.nwp_vfy.nwpc_vfy', ['record_type'], unique=False)
    op.create_table('record.nwp_xp.eps_nwpc_qu',
    sa.Column('repo_id', sa.Integer(), nullable=False),
    sa.Column('version_id', sa.Integer(), nullable=False),
    sa.Column('line_no', sa.Integer(), nullable=False),
    sa.Column('record_type', sa.String(length=100), nullable=True),
    sa.Column('record_date', sa.Date(), nullable=True),
    sa.Column('record_time', sa.Time(), nullable=True),
    sa.Column('record_command', sa.String(length=100), nullable=True),
    sa.Column('record_fullname', sa.String(length=200), nullable=True),
    sa.Column('record_additional_information', sa.Text(), nullable=True),
    sa.Column('record_string', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('repo_id', 'version_id', 'line_no')
    )
    op.create_index('nwp_xp_eps_nwpc_qu_command_index', 'record.nwp_xp.eps_nwpc_qu', ['record_command'], unique=False)
    op.create_index('nwp_xp_eps_nwpc_qu_date_time_index', 'record.nwp_xp.eps_nwpc_qu', ['record_date', 'record_time'], unique=False)
    op.create_index('nwp_xp_eps_nwpc_qu_fullname_index', 'record.nwp_xp.eps_nwpc_qu', ['record_fullname'], unique=False)
    op.create_index('nwp_xp_eps_nwpc_qu_type_index', 'record.nwp_xp.eps_nwpc_qu', ['record_type'], unique=False)
    op.create_table('record.nwp_xp.nwpc_op',
    sa.Column('repo_id', sa.Integer(), nullable=False),
    sa.Column('version_id', sa.Integer(), nullable=False),
    sa.Column('line_no', sa.Integer(), nullable=False),
    sa.Column('record_type', sa.String(length=100), nullable=True),
    sa.Column('record_date', sa.Date(), nullable=True),
    sa.Column('record_time', sa.Time(), nullable=True),
    sa.Column('record_command', sa.String(length=100), nullable=True),
    sa.Column('record_fullname', sa.String(length=200), nullable=True),
    sa.Column('record_additional_information', sa.Text(), nullable=True),
    sa.Column('record_string', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('repo_id', 'version_id', 'line_no')
    )
    op.create_index('nwp_xp_nwpc_op_command_index', 'record.nwp_xp.nwpc_op', ['record_command'], unique=False)
    op.create_index('nwp_xp_nwpc_op_date_time_index', 'record.nwp_xp.nwpc_op', ['record_date', 'record_time'], unique=False)
    op.create_index('nwp_xp_nwpc_op_fullname_index', 'record.nwp_xp.nwpc_op', ['record_fullname'], unique=False)
    op.create_index('nwp_xp_nwpc_op_type_index', 'record.nwp_xp.nwpc_op', ['record_type'], unique=False)
    op.create_table('record.nwp_xp.nwpc_pd',
    sa.Column('repo_id', sa.Integer(), nullable=False),
    sa.Column('version_id', sa.Integer(), nullable=False),
    sa.Column('line_no', sa.Integer(), nullable=False),
    sa.Column('record_type', sa.String(length=100), nullable=True),
    sa.Column('record_date', sa.Date(), nullable=True),
    sa.Column('record_time', sa.Time(), nullable=True),
    sa.Column('record_command', sa.String(length=100), nullable=True),
    sa.Column('record_fullname', sa.String(length=200), nullable=True),
    sa.Column('record_additional_information', sa.Text(), nullable=True),
    sa.Column('record_string', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('repo_id', 'version_id', 'line_no')
    )
    op.create_index('nwp_xp_nwpc_pd_command_index', 'record.nwp_xp.nwpc_pd', ['record_command'], unique=False)
    op.create_index('nwp_xp_nwpc_pd_date_time_index', 'record.nwp_xp.nwpc_pd', ['record_date', 'record_time'], unique=False)
    op.create_index('nwp_xp_nwpc_pd_fullname_index', 'record.nwp_xp.nwpc_pd', ['record_fullname'], unique=False)
    op.create_index('nwp_xp_nwpc_pd_type_index', 'record.nwp_xp.nwpc_pd', ['record_type'], unique=False)
    op.create_table('record.nwp_xp.nwpc_qu',
    sa.Column('repo_id', sa.Integer(), nullable=False),
    sa.Column('version_id', sa.Integer(), nullable=False),
    sa.Column('line_no', sa.Integer(), nullable=False),
    sa.Column('record_type', sa.String(length=100), nullable=True),
    sa.Column('record_date', sa.Date(), nullable=True),
    sa.Column('record_time', sa.Time(), nullable=True),
    sa.Column('record_command', sa.String(length=100), nullable=True),
    sa.Column('record_fullname', sa.String(length=200), nullable=True),
    sa.Column('record_additional_information', sa.Text(), nullable=True),
    sa.Column('record_string', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('repo_id', 'version_id', 'line_no')
    )
    op.create_index('nwp_xp_nwpc_qu_command_index', 'record.nwp_xp.nwpc_qu', ['record_command'], unique=False)
    op.create_index('nwp_xp_nwpc_qu_date_time_index', 'record.nwp_xp.nwpc_qu', ['record_date', 'record_time'], unique=False)
    op.create_index('nwp_xp_nwpc_qu_fullname_index', 'record.nwp_xp.nwpc_qu', ['record_fullname'], unique=False)
    op.create_index('nwp_xp_nwpc_qu_type_index', 'record.nwp_xp.nwpc_qu', ['record_type'], unique=False)
    op.create_table('repo',
    sa.Column('repo_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('repo_name', sa.String(length=45), nullable=True),
    sa.Column('repo_type', sa.String(length=45), nullable=True),
    sa.PrimaryKeyConstraint('repo_id')
    )
    op.create_table('repo_version',
    sa.Column('repo_id', sa.Integer(), nullable=False),
    sa.Column('version_id', sa.String(length=20), nullable=False),
    sa.Column('version_name', sa.String(length=100), nullable=True),
    sa.Column('version_location', sa.String(length=200), nullable=True),
    sa.Column('head_line', sa.Text(), nullable=True),
    sa.Column('collector_id', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('repo_id', 'version_id')
    )
    op.create_table('sms_repo',
    sa.Column('repo_id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('repo_name', sa.String(length=45), nullable=True),
    sa.Column('repo_location', sa.String(length=200), nullable=True),
    sa.Column('current_version_id', sa.String(length=20), nullable=True),
    sa.Column('repo_description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('repo_id')
    )
    op.create_table('user',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.String(length=45), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('sms_repo')
    op.drop_table('repo_version')
    op.drop_table('repo')
    op.drop_index('nwp_xp_nwpc_qu_type_index', table_name='record.nwp_xp.nwpc_qu')
    op.drop_index('nwp_xp_nwpc_qu_fullname_index', table_name='record.nwp_xp.nwpc_qu')
    op.drop_index('nwp_xp_nwpc_qu_date_time_index', table_name='record.nwp_xp.nwpc_qu')
    op.drop_index('nwp_xp_nwpc_qu_command_index', table_name='record.nwp_xp.nwpc_qu')
    op.drop_table('record.nwp_xp.nwpc_qu')
    op.drop_index('nwp_xp_nwpc_pd_type_index', table_name='record.nwp_xp.nwpc_pd')
    op.drop_index('nwp_xp_nwpc_pd_fullname_index', table_name='record.nwp_xp.nwpc_pd')
    op.drop_index('nwp_xp_nwpc_pd_date_time_index', table_name='record.nwp_xp.nwpc_pd')
    op.drop_index('nwp_xp_nwpc_pd_command_index', table_name='record.nwp_xp.nwpc_pd')
    op.drop_table('record.nwp_xp.nwpc_pd')
    op.drop_index('nwp_xp_nwpc_op_type_index', table_name='record.nwp_xp.nwpc_op')
    op.drop_index('nwp_xp_nwpc_op_fullname_index', table_name='record.nwp_xp.nwpc_op')
    op.drop_index('nwp_xp_nwpc_op_date_time_index', table_name='record.nwp_xp.nwpc_op')
    op.drop_index('nwp_xp_nwpc_op_command_index', table_name='record.nwp_xp.nwpc_op')
    op.drop_table('record.nwp_xp.nwpc_op')
    op.drop_index('nwp_xp_eps_nwpc_qu_type_index', table_name='record.nwp_xp.eps_nwpc_qu')
    op.drop_index('nwp_xp_eps_nwpc_qu_fullname_index', table_name='record.nwp_xp.eps_nwpc_qu')
    op.drop_index('nwp_xp_eps_nwpc_qu_date_time_index', table_name='record.nwp_xp.eps_nwpc_qu')
    op.drop_index('nwp_xp_eps_nwpc_qu_command_index', table_name='record.nwp_xp.eps_nwpc_qu')
    op.drop_table('record.nwp_xp.eps_nwpc_qu')
    op.drop_index('nwp_vfy_nwpc_vfy_type_index', table_name='record.nwp_vfy.nwpc_vfy')
    op.drop_index('nwp_vfy_nwpc_vfy_fullname_index', table_name='record.nwp_vfy.nwpc_vfy')
    op.drop_index('nwp_vfy_nwpc_vfy_date_time_index', table_name='record.nwp_vfy.nwpc_vfy')
    op.drop_index('nwp_vfy_nwpc_vfy_command_index', table_name='record.nwp_vfy.nwpc_vfy')
    op.drop_table('record.nwp_vfy.nwpc_vfy')
    op.drop_index('nwp_pos_nwpc_sp_type_index', table_name='record.nwp_pos.nwpc_sp')
    op.drop_index('nwp_pos_nwpc_sp_fullname_index', table_name='record.nwp_pos.nwpc_sp')
    op.drop_index('nwp_pos_nwpc_sp_date_time_index', table_name='record.nwp_pos.nwpc_sp')
    op.drop_index('nwp_pos_nwpc_sp_command_index', table_name='record.nwp_pos.nwpc_sp')
    op.drop_table('record.nwp_pos.nwpc_sp')
    op.drop_table('record')
    # ### end Alembic commands ###
