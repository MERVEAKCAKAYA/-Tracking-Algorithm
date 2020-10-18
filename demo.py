from mosse import mosse
import cv2

sigma=75.
lr=0.125
save_video=False

def select(frame):
 
    bbox=cv2.selectROI("Tracker",frame,False,False)
    return bbox

def reset(frame):
    bbox = select(frame)
    tracker=mosse(frame,bbox,sigma,lr)
    return tracker

if __name__ == '__main__':
    name="flyboard2"
    a="/home/tuhage/Downloads/"+name+".mp4"

    #a = 0
    cap = cv2.VideoCapture(a)
    w = cap.get(cv2.CAP_PROP_FRAME_WIDTH);
    h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT);
    if save_video: 
        fourcc = cv2.VideoWriter_fourcc(*'MP4V')
        out = cv2.VideoWriter(name+".mp4", fourcc, 30, (int(w),int(h)))
    for x in range(1,3):
    	success, frame = cap.read()

    

    height = frame.shape[0]
    width  = frame.shape[1]

    xc, yc = width / 2, height / 2

    bbox = select(frame)

    tracker=mosse(frame,bbox,sigma,lr)
    while True:
        success, frame = cap.read()
        
        try:
            current_frame=tracker.update(frame)
        except Exception as e:
            raise e
            break
        if len(current_frame)!=0:
            cv2.imshow("Tracker", current_frame)
        else:
            tracker=reset(frame)
        if save_video:
            out.write(current_frame)
        cv2.waitKey(1)
        if cv2.waitKey(10) & 0xFF == 110:
            tracker=reset(frame)
    out.release()
