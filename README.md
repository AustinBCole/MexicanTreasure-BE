# **Mexican Treasure BE with Django**
A project to learn to make a BE for multiplayer CYOA games, using Python and Django.

## **Trello Set Up:**

1. Set up Trello board
2. Populate To Do list with MVP features
3. Put extra features in the backlog list
4. Add Trello URL to this README.md file: https://trello.com/b/H15DbdUA/mexican-treasure


## **MVP Features:**

### **Build The BE:**

Include necessary elements such as:

1. A user model
  - user_uuid
  - username
  - password
  - has_active_session: Bool
    - If the user has an active session, then the last item of the session_history array will be the active session. If the user has an active multiplayer session, cannot create new multiplayer session.
  - sessions: Array of sessions
  
2. A session model
  - session_uuid: session's uuid
  - session_status: object containing
    - host_user_status:
      - host_user_uuid
      - current_scene
      - current_stats
      - current_inventory
    - guest_user_status:
      - guest_user_uuid
      - current_scene
      - current_stats
      - current_inventory 

3. Endpoints
  - create user
    - create user object in database
  - update user status
    - Update user status in database(has_active session, sessions)
  - create session
    - Create new session in database
  - Update session status
    - Update existing session in in database(host and guest user inventory, scene, stats
  - abort session
    - Set has_active_session of users to false
  

# **Stretch Goals**

1. Write a how-to guide or blog post that walks readers through the work done to implement this project
