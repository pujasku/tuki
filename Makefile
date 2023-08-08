# Makefile


install:
	@ echo 'Installing dependences'
	@ pip install -r requirements.txt
	@ echo 'You would like to run tuki from an alias, type the following command to do it'
	@ echo 'alias tuki='\''python ${SCRIPT_DIR}/scripts/main.py'



