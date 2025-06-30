# Mergington High School Activities

A comprehensive web application for managing extracurricular activities at Mergington High School. The system provides teachers with tools to view, search, filter, and manage student registrations for various school activities.

## Features

### Activity Management
- **Browse Activities**: View all available extracurricular activities with detailed information
- **Advanced Search**: Search activities by name, description, or keywords
- **Multi-level Filtering**: 
  - **Category filters**: Sports, Arts, Academic, Community, Technology
  - **Day filters**: Filter by specific days of the week (Monday-Sunday) or weekends
  - **Time filters**: Before School, After School, Weekend activities
- **Detailed Scheduling**: View precise timing, days, and participant information for each activity

### Registration Management
- **Teacher Authentication**: Secure login system for teachers and administrators
- **Student Registration**: Teachers can register students for activities using student email addresses
- **Registration Removal**: Teachers can unregister students from activities
- **Participant Tracking**: View current participant counts and manage capacity limits

### User Interface
- **Responsive Design**: Modern, mobile-friendly interface that works on all devices
- **Real-time Updates**: Dynamic loading and filtering without page refreshes
- **Professional Layout**: Clean sidebar navigation with comprehensive filtering options
- **User-friendly Forms**: Modal-based registration forms with validation

### Technical Features
- **RESTful API**: FastAPI-based backend with comprehensive endpoints
- **Database Integration**: MongoDB for persistent data storage
- **Authentication System**: Role-based access control for teachers and administrators
- **Data Validation**: Comprehensive input validation and error handling

## Activity Categories

The system supports diverse extracurricular activities across multiple categories:

- **Sports**: Soccer Team, Basketball Team, Morning Fitness
- **Arts**: Art Club, Drama Club
- **Academic**: Chess Club, Math Club, Debate Team, Science Olympiad
- **Technology**: Programming Class, Weekend Robotics Workshop
- **Competitions**: Sunday Chess Tournament

## Scheduling

Activities are scheduled throughout the week including:
- **Early Morning**: Programs starting as early as 6:30 AM
- **After School**: Activities from 3:15 PM to 5:30 PM
- **Weekend Programs**: Saturday and Sunday activities
- **Flexible Timing**: Various durations from 45 minutes to 4 hours

## Development Guide

For detailed setup and development instructions, please refer to our [Development Guide](../docs/how-to-develop.md).
