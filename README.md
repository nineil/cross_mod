# cross_mod dataset

### Data
Our data is composed of two files: ads.zip and coco.zip. Both files can be downloaded running download.sh script.

Each dataset is composed of two folders ims and bv, and a data.csv file. Ims folder contains images for our experiment, and bv folder contains the bubble_view visualizations (gaze maps). Also, data.csv contains the fields:

- task_id: identifier for task submitted to amazon mechanical turk.
- image: image name.
- ad_msg: text for image annotation or ad message.
- personality: vector for personality survey.
- mturker_id: identifier of amazon mechanical turk worker.

### Example
