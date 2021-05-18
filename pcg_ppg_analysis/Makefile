.PHONY: docs 
docs:
	rm -rf docs/
	pdoc --html --output-dir docs --config show_source_code=True --config latex_math=True --force pcg_ppg_analysis
	mv docs/pcg_ppg_analysis/* docs
	rmdir docs/pcg_ppg_analysis