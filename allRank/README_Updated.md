# allRank : Learning to Rank in PyTorch

### Getting started guide

This is an updateed README file modified from original README.md from  Allegro allrank repository.

To start, we need train.txt, test.txt and valid.txt created using 'dump_svmlight_file command' in FeatureSelection notebook

There are 2 ways to run allRank, with and without docker.

## Without docker by creating conda virtual environment using environment_allRank.yml

conda env create -f environment_allRank.yml
conda activate environment_allrank

To train your own model, configure your experiment in ```config.json``` file and run  

```python allrank/main.py --config_file_name config.json --run_id <the_name_of_your_experiment> --job_dir <the_place_to_save_results>```

Within allRank directory, one needs config.json.
Run following command from bash/powershell terminal

python -m allrank.main --config-file-name config.json --run-id val_C2norank1b.json --job-dir task_C2norank1b

Python run main.py within 'allrank' folder using config.json at same root level. 
This command creates new folder "task_c1" at same root level. Within "tast_c1", results are stored including training.log, used_config 

## with docker 

This is explained in the original README.md

## License

Apache 2 License
