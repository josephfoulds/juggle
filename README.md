# Blog Engine

Blog Engine is a technical assessment for Juggle Jobs

## Overview
Project is currently implemented using SQLite as in-built relational database store. Considering the time constraints to produce MVP this seemed more logical than rolling out a cloud based SQL server (eg, AWS RDS) although this would be preference in production.

Blogging engine is designed in Django using a RESTful API to access and delete associated resources.

_nb: No authentication is performed on the API in line with project spec._

## Installation
[TODO]

## Internal API
All APIs are designed RESTful-y and use standard HTTP methods (GET, POST, DELETE) for updating and fetching resource information
### Engine Resources
* `GET /` - Display all blogs

### Blog Resources
* `POST /blog/` - Create new blog
* `GET /blog/[BLOG_ID]/` - Show all posts on blog
* `DELETE /blog/[BLOG_ID]/` - Delete blog

### Post Resources
* `POST /blog/[BLOG_ID]/post/` - Create new post
* `GET /blog/[BLOG_ID]/post/[POST_ID]` - Show post data + comments
* `DELETE /blog/[BLOG_ID]/post/[POST_ID]` - Delete post

### Comment Resources
* `POST /blog/[BLOG_ID]/post/[POST_ID]/comment` - Create new comment
* `DELETE /blog/[BLOG_ID]/post/[POST_ID]/comment/[COMMENT_ID]` - Delete comment


## Schema

|       Blog        |
| ----------------- |
| id (primary key)  |
| name (CharField)  |

|       Post           |
| -------------------- |
| id (primary key)     |
| blog (foreign key)   |
| content (CharField)  |
| name (CharField)     |

|    Comment           |
| -------------------- |
| id (primary key)     |
| post (foreign key)   |
| content (CharField)  |
| author (CharField)   |


## Future Integrations
### Caching
* Blog system would benefit from page caching in order to reduce database throughput and latency for read requests. 

* Would suggest integrating a page caching system using in-memory storage (such as Redis) with cache invalidation on write API requests to relevant data stores

### RESTful expansion
* API design allows for easy integration of additional functionality such as PATCH HTTP methods for updating blog/post/comment information