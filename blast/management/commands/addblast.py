from blast.models import BlastDb,SequenceType
from django.core.management.base import BaseCommand
#from app.models import Organism
import sys
#sys.path.append('genomics-workspace/app/management/commands/add_func.py')
from add_func import get_organism, display_name, get_path, get_type

class Command(BaseCommand):

    def add_arguments(self,parser):
        parser.add_argument('Genus_Species',nargs='+',type=str)
        parser.add_argument('-t','--type',nargs='+',type=str,help='please enter nucleotide or peptide and enter Genome Assembly or Protein or Transcript')
        parser.add_argument('-f','--filename',nargs=1,type=str)

    def handle(self,*args,**options):

        name=display_name(options)
        organism = get_organism(name)
        if organism:#check whether organism is exist or not

            blast_type = get_type(options)
            title = options['filename'][0]
            fasta_file_path = get_path('blast',title)
            new_db = BlastDb(organism = organism, type = blast_type, fasta_file = fasta_file_path, title = title, description = '', is_shown = True )
            new_db.save()
            print("you can move to makeblastdb and populate sequence step")
            #except django.db.utils.IntegrityError:
                #print("This database already exists")
                #sys.exit(0)
        else :
            pass
            #TODO can use subprocess lib here to add new organism
