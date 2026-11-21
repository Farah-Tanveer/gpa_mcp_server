import os

from fastmcp import FastMCP

from tools import (
    get_credit_hours,
    marks_to_grade_points,
    calculate_semester_gpa,
    calculate_new_cgpa,
    required_gpa_for_target,
    get_semester_courses,
    get_remaining_credit_hours,
    save_report,
)

mcp = FastMCP("cgpa")

for tool in (
    get_credit_hours,
    marks_to_grade_points,
    calculate_semester_gpa,
    calculate_new_cgpa,
    required_gpa_for_target,
    get_semester_courses,
    get_remaining_credit_hours,
    save_report,
):
    mcp.tool(tool)

if __name__ == "__main__":
    # PORT is set by most hosting services; locally it falls back to 8000
    port = int(os.environ.get("PORT", 8000))
    host = os.environ.get("HOST", "127.0.0.1")
    mcp.run(transport="http", host=host, port=port, path="/mcp")