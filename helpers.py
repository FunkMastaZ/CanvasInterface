import datetime
import re

# Searches a list of assignments for a particular type
def assignment_finder_by_type(target_type, list_of_assignments):
    list_of_matching_assignments = []
    # For each assignment in the list of course assignments...
    for assignment in list_of_assignments:
        # ...if one of the submission types matches the type specified...
        # ...and it's not the Roll Call Attendance assignment...
        if target_type in assignment.submission_types and "Roll Call Attendance" not in assignment.name:
            # ...then add this assignment to a list of other found assignments
            list_of_matching_assignments.append(assignment)
    # Finally, return the list of matching assignments
    return list_of_matching_assignments

# Searches a list of assignments for something that may be a Turnitin assignment
def turnitin_assignment_finder(list_of_assignments):
    list_of_matching_assignments = []
    # For each assignment in the list of course assignments...
    for assignment in list_of_assignments:
        # ...if one of the submission types matches the type specified...
        # ...and it's not the Roll Call Attendance assignment...
        if "external_tool" in assignment.submission_types and "Roll Call Attendance" not in assignment.name:
            #  ...check if the word "Turnitin" exists in the external URL attribute for this assignment...
            if "turnitin" in assignment.external_tool_tag_attributes['url']:
                # ...if so, then add this assignment to a list of other found assignments.
                list_of_matching_assignments.append(assignment)
    # Finally, return the list of matching assignments
    return list_of_matching_assignments


# Searches PageViews for a specific user for a query term in a certain attribute
# Searches a range of time based on "days to look back"
def search_pageviews(user, query, attribute='url', days_to_look_back=90):
    matching_pageviews =[]
    list_of_pageviews = user.get_page_views(start_time=(datetime.datetime.now() - datetime.timedelta(days=days_to_look_back)))
    for view in list_of_pageviews:
        if query in getattr(view, attribute):
            matching_pageviews.append(view)
    return matching_pageviews


# For verifying the correctness of course ID entries (generally when users provide search terms)
# E.g. ABC1101.001F17
def validate_sis_course_id(course_id):
    # If the input matches the correct alpha-numeric format...
    if re.match('^[A-Za-z]{3}[\d]{4}\.[\d]{3}[A-Za-z][\d]{2}', course_id):
        # ...then return true
        return True
    # Else the format is not correct...
    else:
        # ...then return false
        return False


# E.g. 1234567
def validate_canvas_course_id(course_id):
    # If the input matches the correct alpha-numeric format...
    if re.match('^[\d]{7}', course_id):
        # ...then return true
        return True
    # Else the format is not correct...
    else:
        # ...then return false
        return False
