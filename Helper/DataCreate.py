def Create(Day, Hours, Min, cur_lane_value_pre, left_lane_value_pre,right_lane_value_pre, front_lane_value_pre, Image_Rec_Count, Pre_sig_Count):
    data = {'Day' : Day,	\
            'Hours' : Hours, \
            'Min' : Min, 	\
            'Count_Lane_1' : (cur_lane_value_pre+Image_Rec_Count[0]+Pre_sig_Count[0])//3,
            'Count_Lane_2' : (left_lane_value_pre+Image_Rec_Count[1]+Pre_sig_Count[1])//3,
            'Count_Lane_3' : (right_lane_value_pre+Image_Rec_Count[2]+Pre_sig_Count[2])//3,
            'Count_Lane_4' : (front_lane_value_pre+Image_Rec_Count[3]+Pre_sig_Count[3])//3
            }
    return data
