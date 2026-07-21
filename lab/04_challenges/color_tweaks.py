COLOR_RANGES = {
    'red_low':  ([0,   50, 50], [10,  255, 255]),
    'red_high': ([165, 50, 50], [179, 255, 255]),
    'orange':   ([8,   50, 50], [18,  255, 255]),
    'green':    ([60,  50, 50], [85,  255, 255]),
}

def detect_color(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # red needs two masks
    mask_red = cv2.bitwise_or(
        cv2.inRange(hsv, np.array(COLOR_RANGES['red_low'][0]),  np.array(COLOR_RANGES['red_low'][1])),
        cv2.inRange(hsv, np.array(COLOR_RANGES['red_high'][0]), np.array(COLOR_RANGES['red_high'][1]))
    )
    counts = {
        'red':    cv2.countNonZero(mask_red),
        'orange': cv2.countNonZero(cv2.inRange(hsv, np.array(COLOR_RANGES['orange'][0]), np.array(COLOR_RANGES['orange'][1]))),
        'green':  cv2.countNonZero(cv2.inRange(hsv, np.array(COLOR_RANGES['green'][0]),  np.array(COLOR_RANGES['green'][1]))),
    }
    
    best_color = max(counts, key=counts.get)
    return best_color if counts[best_color] > 500 else None
