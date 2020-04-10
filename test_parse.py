import argparse
# https://click.palletsprojects.com/en/7.x/


parser = argparse.ArgumentParser(description="Odoo Environment")

parser.add_argument('-V',action='version',version='test parse backup V1.0')
bkp = parser.add_subparsers(help='Comandos de restauracion')

bkp.add_parser('restore',help='restaurar base de datos')
bkp.add_subparser('cc',help='cola')

args = parser.parse_args()

probar esto

