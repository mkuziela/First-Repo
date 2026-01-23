import urllib.request
import os
import tarfile

MODEL_URL = "http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v2_coco_2018_03_29.tar.gz"
CONFIG_URL = "https://raw.githubusercontent.com/opencv/opencv_extra/master/testdata/dnn/ssd_mobilenet_v2_coco_2018_03_29.pbtxt"


def download_models():
    print("Pobieranie modelu MobileNet SSD (może to chwilę potrwać)...")

    if not os.path.exists("ssd_mobilenet_v2_coco.pbtxt"):
        urllib.request.urlretrieve(CONFIG_URL, "ssd_mobilenet_v2_coco.pbtxt")
        print("Pobrano config (.pbtxt)")

    if not os.path.exists("ssd_mobilenet_v2_coco_2018_03_29.tar.gz"):
        urllib.request.urlretrieve(MODEL_URL, "ssd_mobilenet_v2_coco_2018_03_29.tar.gz")

    print("Rozpakowywanie...")
    with tarfile.open("ssd_mobilenet_v2_coco_2018_03_29.tar.gz", "r:gz") as tar:

        def is_within_directory(directory, target):
            abs_directory = os.path.abspath(directory)
            abs_target = os.path.abspath(target)
            prefix = os.path.commonprefix([abs_directory, abs_target])
            return prefix == abs_directory

        def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
            for member in tar.getmembers():
                member_path = os.path.join(path, member.name)
                if not is_within_directory(path, member_path):
                    raise Exception("Attempted Path Traversal in Tar File")
            tar.extractall(path, members, numeric_owner=numeric_owner)

        safe_extract(tar)

    source_pb = "ssd_mobilenet_v2_coco_2018_03_29/frozen_inference_graph.pb"
    if os.path.exists(source_pb):
        os.replace(source_pb, "frozen_inference_graph.pb")
        print("Model gotowy: frozen_inference_graph.pb")

    if os.path.exists("ssd_mobilenet_v2_coco_2018_03_29"):
        import shutil
        shutil.rmtree("ssd_mobilenet_v2_coco_2018_03_29")


if __name__ == "__main__":
    download_models()