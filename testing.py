from cli_main import main
main.helpers.Core()
print(dir(main))
print(main.main_root)
print(main.get_project_root())

helpers_list = (dir(main.helpers))
core_list = (dir(main.helpers.Core))

main.helpers.get_detector_stuff() 

# print(detect_model_locs)
''' ############################################################################################ '''
# pix2pix(self, dataset_path, images_set_name, epochs=2, loops=2, mode='train', first_run=True)
''' ############################################################################################ '''