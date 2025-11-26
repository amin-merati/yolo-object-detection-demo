import argparse
from pathlib import Path

from ultralytics import YOLO


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Simple YOLOv8 object detection demo using Ultralytics."
    )
    parser.add_argument(
        "--source",
        type=str,
        required=True,
        help="Image path or URL, e.g. 'image.jpg' or 'https://ultralytics.com/images/bus.jpg'",
    )
    parser.add_argument(
        "--model",
        type=str,
        default="yolov8n.pt",
        help="YOLOv8 model file to use (default: yolov8n.pt).",
    )
    parser.add_argument(
        "--device",
        type=str,
        default="cpu",
        help="Device to run on, e.g. 'cpu' or '0' for first CUDA GPU.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    print(f"[INFO] Loading YOLO model: {args.model}")
    model = YOLO(args.model)  # Will auto-download from Ultralytics hub if needed

    print(f"[INFO] Running detection on source: {args.source}")
    results = model.predict(
        source=args.source,
        device=args.device,
        save=True,           # save images with bounding boxes
        save_txt=False,      # set True if you want label txt files
        verbose=True,
    )

    # Ultralytics returns a list of Result objects; saved images are reported there
    out_dirs = {Path(r.save_dir) for r in results}
    for d in out_dirs:
        print(f"[INFO] Output saved to: {d.resolve()}")


if __name__ == "__main__":
    main()

