all:
	@echo "make clean cleans up"

clean:
	rm -rf vupy.egg-info
	rm -rf dist 
	rm -f python-vupy*.rpm
