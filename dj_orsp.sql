/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 100137
 Source Host           : localhost:3306
 Source Schema         : dj_orsp

 Target Server Type    : MySQL
 Target Server Version : 100137
 File Encoding         : 65001

 Date: 23/04/2019 19:12:41
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq`(`group_id`, `permission_id`) USING BTREE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq`(`content_type_id`, `codename`) USING BTREE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 101 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO `auth_permission` VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO `auth_permission` VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO `auth_permission` VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO `auth_permission` VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO `auth_permission` VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO `auth_permission` VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO `auth_permission` VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO `auth_permission` VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO `auth_permission` VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO `auth_permission` VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO `auth_permission` VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO `auth_permission` VALUES (13, 'Can add user', 4, 'add_user');
INSERT INTO `auth_permission` VALUES (14, 'Can change user', 4, 'change_user');
INSERT INTO `auth_permission` VALUES (15, 'Can delete user', 4, 'delete_user');
INSERT INTO `auth_permission` VALUES (16, 'Can view user', 4, 'view_user');
INSERT INTO `auth_permission` VALUES (17, 'Can add content type', 5, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (18, 'Can change content type', 5, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (19, 'Can delete content type', 5, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (20, 'Can view content type', 5, 'view_contenttype');
INSERT INTO `auth_permission` VALUES (21, 'Can add session', 6, 'add_session');
INSERT INTO `auth_permission` VALUES (22, 'Can change session', 6, 'change_session');
INSERT INTO `auth_permission` VALUES (23, 'Can delete session', 6, 'delete_session');
INSERT INTO `auth_permission` VALUES (24, 'Can view session', 6, 'view_session');
INSERT INTO `auth_permission` VALUES (25, 'Can add address', 7, 'add_address');
INSERT INTO `auth_permission` VALUES (26, 'Can change address', 7, 'change_address');
INSERT INTO `auth_permission` VALUES (27, 'Can delete address', 7, 'delete_address');
INSERT INTO `auth_permission` VALUES (28, 'Can view address', 7, 'view_address');
INSERT INTO `auth_permission` VALUES (29, 'Can add admin msg', 8, 'add_adminmsg');
INSERT INTO `auth_permission` VALUES (30, 'Can change admin msg', 8, 'change_adminmsg');
INSERT INTO `auth_permission` VALUES (31, 'Can delete admin msg', 8, 'delete_adminmsg');
INSERT INTO `auth_permission` VALUES (32, 'Can view admin msg', 8, 'view_adminmsg');
INSERT INTO `auth_permission` VALUES (33, 'Can add city', 9, 'add_city');
INSERT INTO `auth_permission` VALUES (34, 'Can change city', 9, 'change_city');
INSERT INTO `auth_permission` VALUES (35, 'Can delete city', 9, 'delete_city');
INSERT INTO `auth_permission` VALUES (36, 'Can view city', 9, 'view_city');
INSERT INTO `auth_permission` VALUES (37, 'Can add info', 10, 'add_info');
INSERT INTO `auth_permission` VALUES (38, 'Can change info', 10, 'change_info');
INSERT INTO `auth_permission` VALUES (39, 'Can delete info', 10, 'delete_info');
INSERT INTO `auth_permission` VALUES (40, 'Can view info', 10, 'view_info');
INSERT INTO `auth_permission` VALUES (41, 'Can add province', 11, 'add_province');
INSERT INTO `auth_permission` VALUES (42, 'Can change province', 11, 'change_province');
INSERT INTO `auth_permission` VALUES (43, 'Can delete province', 11, 'delete_province');
INSERT INTO `auth_permission` VALUES (44, 'Can view province', 11, 'view_province');
INSERT INTO `auth_permission` VALUES (45, 'Can add user', 12, 'add_user');
INSERT INTO `auth_permission` VALUES (46, 'Can change user', 12, 'change_user');
INSERT INTO `auth_permission` VALUES (47, 'Can delete user', 12, 'delete_user');
INSERT INTO `auth_permission` VALUES (48, 'Can view user', 12, 'view_user');
INSERT INTO `auth_permission` VALUES (49, 'Can add collect', 13, 'add_collect');
INSERT INTO `auth_permission` VALUES (50, 'Can change collect', 13, 'change_collect');
INSERT INTO `auth_permission` VALUES (51, 'Can delete collect', 13, 'delete_collect');
INSERT INTO `auth_permission` VALUES (52, 'Can view collect', 13, 'view_collect');
INSERT INTO `auth_permission` VALUES (53, 'Can add download', 14, 'add_download');
INSERT INTO `auth_permission` VALUES (54, 'Can change download', 14, 'change_download');
INSERT INTO `auth_permission` VALUES (55, 'Can delete download', 14, 'delete_download');
INSERT INTO `auth_permission` VALUES (56, 'Can view download', 14, 'view_download');
INSERT INTO `auth_permission` VALUES (57, 'Can add resource', 15, 'add_resource');
INSERT INTO `auth_permission` VALUES (58, 'Can change resource', 15, 'change_resource');
INSERT INTO `auth_permission` VALUES (59, 'Can delete resource', 15, 'delete_resource');
INSERT INTO `auth_permission` VALUES (60, 'Can view resource', 15, 'view_resource');
INSERT INTO `auth_permission` VALUES (61, 'Can add resource type', 16, 'add_resourcetype');
INSERT INTO `auth_permission` VALUES (62, 'Can change resource type', 16, 'change_resourcetype');
INSERT INTO `auth_permission` VALUES (63, 'Can delete resource type', 16, 'delete_resourcetype');
INSERT INTO `auth_permission` VALUES (64, 'Can view resource type', 16, 'view_resourcetype');
INSERT INTO `auth_permission` VALUES (65, 'Can add technical field', 17, 'add_technicalfield');
INSERT INTO `auth_permission` VALUES (66, 'Can change technical field', 17, 'change_technicalfield');
INSERT INTO `auth_permission` VALUES (67, 'Can delete technical field', 17, 'delete_technicalfield');
INSERT INTO `auth_permission` VALUES (68, 'Can view technical field', 17, 'view_technicalfield');
INSERT INTO `auth_permission` VALUES (69, 'Can add two technical field', 18, 'add_twotechnicalfield');
INSERT INTO `auth_permission` VALUES (70, 'Can change two technical field', 18, 'change_twotechnicalfield');
INSERT INTO `auth_permission` VALUES (71, 'Can delete two technical field', 18, 'delete_twotechnicalfield');
INSERT INTO `auth_permission` VALUES (72, 'Can view two technical field', 18, 'view_twotechnicalfield');
INSERT INTO `auth_permission` VALUES (73, 'Can add order', 19, 'add_order');
INSERT INTO `auth_permission` VALUES (74, 'Can change order', 19, 'change_order');
INSERT INTO `auth_permission` VALUES (75, 'Can delete order', 19, 'delete_order');
INSERT INTO `auth_permission` VALUES (76, 'Can view order', 19, 'view_order');
INSERT INTO `auth_permission` VALUES (77, 'Can add product_type_one', 20, 'add_product_type_one');
INSERT INTO `auth_permission` VALUES (78, 'Can change product_type_one', 20, 'change_product_type_one');
INSERT INTO `auth_permission` VALUES (79, 'Can delete product_type_one', 20, 'delete_product_type_one');
INSERT INTO `auth_permission` VALUES (80, 'Can view product_type_one', 20, 'view_product_type_one');
INSERT INTO `auth_permission` VALUES (81, 'Can add product_type_three', 21, 'add_product_type_three');
INSERT INTO `auth_permission` VALUES (82, 'Can change product_type_three', 21, 'change_product_type_three');
INSERT INTO `auth_permission` VALUES (83, 'Can delete product_type_three', 21, 'delete_product_type_three');
INSERT INTO `auth_permission` VALUES (84, 'Can view product_type_three', 21, 'view_product_type_three');
INSERT INTO `auth_permission` VALUES (85, 'Can add product_type_two', 22, 'add_product_type_two');
INSERT INTO `auth_permission` VALUES (86, 'Can change product_type_two', 22, 'change_product_type_two');
INSERT INTO `auth_permission` VALUES (87, 'Can delete product_type_two', 22, 'delete_product_type_two');
INSERT INTO `auth_permission` VALUES (88, 'Can view product_type_two', 22, 'view_product_type_two');
INSERT INTO `auth_permission` VALUES (89, 'Can add products', 23, 'add_products');
INSERT INTO `auth_permission` VALUES (90, 'Can change products', 23, 'change_products');
INSERT INTO `auth_permission` VALUES (91, 'Can delete products', 23, 'delete_products');
INSERT INTO `auth_permission` VALUES (92, 'Can view products', 23, 'view_products');
INSERT INTO `auth_permission` VALUES (93, 'Can add status', 24, 'add_status');
INSERT INTO `auth_permission` VALUES (94, 'Can change status', 24, 'change_status');
INSERT INTO `auth_permission` VALUES (95, 'Can delete status', 24, 'delete_status');
INSERT INTO `auth_permission` VALUES (96, 'Can view status', 24, 'view_status');
INSERT INTO `auth_permission` VALUES (97, 'Can add user_collect', 25, 'add_user_collect');
INSERT INTO `auth_permission` VALUES (98, 'Can change user_collect', 25, 'change_user_collect');
INSERT INTO `auth_permission` VALUES (99, 'Can delete user_collect', 25, 'delete_user_collect');
INSERT INTO `auth_permission` VALUES (100, 'Can view user_collect', 25, 'view_user_collect');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `first_name` varchar(30) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `last_name` varchar(150) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `email` varchar(254) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_groups_user_id_group_id_94350c0c_uniq`(`user_id`, `group_id`) USING BTREE,
  INDEX `auth_user_groups_group_id_97559544_fk_auth_group_id`(`group_id`) USING BTREE,
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq`(`user_id`, `permission_id`) USING BTREE,
  INDEX `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext CHARACTER SET utf8 COLLATE utf8_bin,
  `object_repr` varchar(200) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co`(`content_type_id`) USING BTREE,
  INDEX `django_admin_log_user_id_c564eba6_fk_auth_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `model` varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq`(`app_label`, `model`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 26 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (4, 'auth', 'user');
INSERT INTO `django_content_type` VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (13, 'file', 'collect');
INSERT INTO `django_content_type` VALUES (14, 'file', 'download');
INSERT INTO `django_content_type` VALUES (15, 'file', 'resource');
INSERT INTO `django_content_type` VALUES (16, 'file', 'resourcetype');
INSERT INTO `django_content_type` VALUES (17, 'file', 'technicalfield');
INSERT INTO `django_content_type` VALUES (18, 'file', 'twotechnicalfield');
INSERT INTO `django_content_type` VALUES (19, 'resource', 'order');
INSERT INTO `django_content_type` VALUES (20, 'resource', 'product_type_one');
INSERT INTO `django_content_type` VALUES (21, 'resource', 'product_type_three');
INSERT INTO `django_content_type` VALUES (22, 'resource', 'product_type_two');
INSERT INTO `django_content_type` VALUES (23, 'resource', 'products');
INSERT INTO `django_content_type` VALUES (24, 'resource', 'status');
INSERT INTO `django_content_type` VALUES (25, 'resource', 'user_collect');
INSERT INTO `django_content_type` VALUES (6, 'sessions', 'session');
INSERT INTO `django_content_type` VALUES (7, 'user', 'address');
INSERT INTO `django_content_type` VALUES (8, 'user', 'adminmsg');
INSERT INTO `django_content_type` VALUES (9, 'user', 'city');
INSERT INTO `django_content_type` VALUES (10, 'user', 'info');
INSERT INTO `django_content_type` VALUES (11, 'user', 'province');
INSERT INTO `django_content_type` VALUES (12, 'user', 'user');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 19 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES (1, 'contenttypes', '0001_initial', '2019-04-06 16:40:07.017956');
INSERT INTO `django_migrations` VALUES (2, 'auth', '0001_initial', '2019-04-06 16:40:14.059126');
INSERT INTO `django_migrations` VALUES (3, 'admin', '0001_initial', '2019-04-06 16:40:16.695077');
INSERT INTO `django_migrations` VALUES (4, 'admin', '0002_logentry_remove_auto_add', '2019-04-06 16:40:16.733972');
INSERT INTO `django_migrations` VALUES (5, 'admin', '0003_logentry_add_action_flag_choices', '2019-04-06 16:40:16.768879');
INSERT INTO `django_migrations` VALUES (6, 'contenttypes', '0002_remove_content_type_name', '2019-04-06 16:40:17.600654');
INSERT INTO `django_migrations` VALUES (7, 'auth', '0002_alter_permission_name_max_length', '2019-04-06 16:40:18.128273');
INSERT INTO `django_migrations` VALUES (8, 'auth', '0003_alter_user_email_max_length', '2019-04-06 16:40:18.959022');
INSERT INTO `django_migrations` VALUES (9, 'auth', '0004_alter_user_username_opts', '2019-04-06 16:40:19.016867');
INSERT INTO `django_migrations` VALUES (10, 'auth', '0005_alter_user_last_login_null', '2019-04-06 16:40:19.321053');
INSERT INTO `django_migrations` VALUES (11, 'auth', '0006_require_contenttypes_0002', '2019-04-06 16:40:19.351013');
INSERT INTO `django_migrations` VALUES (12, 'auth', '0007_alter_validators_add_error_messages', '2019-04-06 16:40:19.395853');
INSERT INTO `django_migrations` VALUES (13, 'auth', '0008_alter_user_username_max_length', '2019-04-06 16:40:20.027170');
INSERT INTO `django_migrations` VALUES (14, 'auth', '0009_alter_user_last_name_max_length', '2019-04-06 16:40:20.866924');
INSERT INTO `django_migrations` VALUES (15, 'user', '0001_initial', '2019-04-06 16:40:28.648114');
INSERT INTO `django_migrations` VALUES (16, 'file', '0001_initial', '2019-04-06 16:40:38.541655');
INSERT INTO `django_migrations` VALUES (17, 'resource', '0001_initial', '2019-04-06 16:40:51.110042');
INSERT INTO `django_migrations` VALUES (18, 'sessions', '0001_initial', '2019-04-06 16:40:51.743377');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `session_data` longtext CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_expire_date_a5c62663`(`expire_date`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for file_collect
-- ----------------------------
DROP TABLE IF EXISTS `file_collect`;
CREATE TABLE `file_collect`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `resource_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `file_collect_resource_id_a212cfec_fk_file_resource_id`(`resource_id`) USING BTREE,
  INDEX `file_collect_user_id_44357183_fk_user_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `file_collect_resource_id_a212cfec_fk_file_resource_id` FOREIGN KEY (`resource_id`) REFERENCES `file_resource` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `file_collect_user_id_44357183_fk_user_user_id` FOREIGN KEY (`user_id`) REFERENCES `user_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Records of file_collect
-- ----------------------------
INSERT INTO `file_collect` VALUES (1, 1, 1);

-- ----------------------------
-- Table structure for file_download
-- ----------------------------
DROP TABLE IF EXISTS `file_download`;
CREATE TABLE `file_download`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `file_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `file_download_file_id_2cc5a082_fk_file_resource_id`(`file_id`) USING BTREE,
  INDEX `file_download_user_id_05d59983_fk_user_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `file_download_file_id_2cc5a082_fk_file_resource_id` FOREIGN KEY (`file_id`) REFERENCES `file_resource` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `file_download_user_id_05d59983_fk_user_user_id` FOREIGN KEY (`user_id`) REFERENCES `user_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Records of file_download
-- ----------------------------
INSERT INTO `file_download` VALUES (1, 1, 1);

-- ----------------------------
-- Table structure for file_resource
-- ----------------------------
DROP TABLE IF EXISTS `file_resource`;
CREATE TABLE `file_resource`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(40) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `download_count` int(11) NOT NULL DEFAULT 0,
  `need_integral` int(11) NOT NULL,
  `upload_time` datetime(6) NOT NULL,
  `like_num` int(11) NOT NULL,
  `share_num` int(11) NOT NULL,
  `title` varchar(80) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `describe` varchar(80) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `resourceTypeId_id` int(11) NOT NULL,
  `twoTechnicalFieldId_id` int(11) NOT NULL,
  `upload_user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `file_resource_resourceTypeId_id_aa16bc10_fk_file_resourcetype_id`(`resourceTypeId_id`) USING BTREE,
  INDEX `file_resource_twoTechnicalFieldId__b90c6cfc_fk_file_twot`(`twoTechnicalFieldId_id`) USING BTREE,
  INDEX `file_resource_upload_user_id_115396fa_fk_user_user_id`(`upload_user_id`) USING BTREE,
  CONSTRAINT `file_resource_resourceTypeId_id_aa16bc10_fk_file_resourcetype_id` FOREIGN KEY (`resourceTypeId_id`) REFERENCES `file_resourcetype` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `file_resource_twoTechnicalFieldId__b90c6cfc_fk_file_twot` FOREIGN KEY (`twoTechnicalFieldId_id`) REFERENCES `file_twotechnicalfield` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `file_resource_upload_user_id_115396fa_fk_user_user_id` FOREIGN KEY (`upload_user_id`) REFERENCES `user_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Records of file_resource
-- ----------------------------
INSERT INTO `file_resource` VALUES (1, 'b47f43a6-f250-4e29-a88c-bc220f1ce426.pdf', 0, 5, '2019-04-06 17:08:37.381200', 0, 0, 'Kafka权威指南.pdf', '入门级别书籍', 1, 5, 1);

-- ----------------------------
-- Table structure for file_resourcetype
-- ----------------------------
DROP TABLE IF EXISTS `file_resourcetype`;
CREATE TABLE `file_resourcetype`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Records of file_resourcetype
-- ----------------------------
INSERT INTO `file_resourcetype` VALUES (1, '文档类');
INSERT INTO `file_resourcetype` VALUES (2, '工具类');
INSERT INTO `file_resourcetype` VALUES (3, '代码类');
INSERT INTO `file_resourcetype` VALUES (4, '其他');

-- ----------------------------
-- Table structure for file_technicalfield
-- ----------------------------
DROP TABLE IF EXISTS `file_technicalfield`;
CREATE TABLE `file_technicalfield`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 11 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Records of file_technicalfield
-- ----------------------------
INSERT INTO `file_technicalfield` VALUES (1, '前端');
INSERT INTO `file_technicalfield` VALUES (2, '架构');
INSERT INTO `file_technicalfield` VALUES (3, '区块链');
INSERT INTO `file_technicalfield` VALUES (4, '编程语言');
INSERT INTO `file_technicalfield` VALUES (5, '数据库');
INSERT INTO `file_technicalfield` VALUES (6, '游戏开发');
INSERT INTO `file_technicalfield` VALUES (7, '移动开发');
INSERT INTO `file_technicalfield` VALUES (8, '运维');
INSERT INTO `file_technicalfield` VALUES (9, '人工智能');
INSERT INTO `file_technicalfield` VALUES (10, '大数据');

-- ----------------------------
-- Table structure for file_twotechnicalfield
-- ----------------------------
DROP TABLE IF EXISTS `file_twotechnicalfield`;
CREATE TABLE `file_twotechnicalfield`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `technicalFieldId_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `file_twotechnicalfie_technicalFieldId_id_80ff94c6_fk_file_tech`(`technicalFieldId_id`) USING BTREE,
  CONSTRAINT `file_twotechnicalfie_technicalFieldId_id_80ff94c6_fk_file_tech` FOREIGN KEY (`technicalFieldId_id`) REFERENCES `file_technicalfield` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Records of file_twotechnicalfield
-- ----------------------------
INSERT INTO `file_twotechnicalfield` VALUES (1, 'HTML', 1);
INSERT INTO `file_twotechnicalfield` VALUES (3, 'JS', 1);
INSERT INTO `file_twotechnicalfield` VALUES (4, 'CSS', 1);
INSERT INTO `file_twotechnicalfield` VALUES (5, 'kafka', 10);
INSERT INTO `file_twotechnicalfield` VALUES (6, 'hadoop', 10);

-- ----------------------------
-- Table structure for resource_order
-- ----------------------------
DROP TABLE IF EXISTS `resource_order`;
CREATE TABLE `resource_order`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `unitPrice` decimal(11, 2) NOT NULL,
  `ordertime` datetime(6) NOT NULL,
  `sellernum` int(11) NOT NULL,
  `buyernum` int(11) NOT NULL,
  `status` varchar(10) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `buyer_id` int(11) NOT NULL,
  `buyerAddress_id` int(11) NOT NULL,
  `good_id` int(11) NOT NULL,
  `seller_id` int(11) NOT NULL,
  `sellerAddress_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `resource_order_buyer_id_b56677ee_fk_user_info_id`(`buyer_id`) USING BTREE,
  INDEX `resource_order_buyerAddress_id_5430ac87_fk_user_address_id`(`buyerAddress_id`) USING BTREE,
  INDEX `resource_order_good_id_eb80855a_fk_resource_products_id`(`good_id`) USING BTREE,
  INDEX `resource_order_seller_id_ff847c14_fk_user_info_id`(`seller_id`) USING BTREE,
  INDEX `resource_order_sellerAddress_id_7ee1008a_fk_user_address_id`(`sellerAddress_id`) USING BTREE,
  CONSTRAINT `resource_order_buyerAddress_id_5430ac87_fk_user_address_id` FOREIGN KEY (`buyerAddress_id`) REFERENCES `user_address` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `resource_order_buyer_id_b56677ee_fk_user_info_id` FOREIGN KEY (`buyer_id`) REFERENCES `user_info` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `resource_order_good_id_eb80855a_fk_resource_products_id` FOREIGN KEY (`good_id`) REFERENCES `resource_products` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `resource_order_sellerAddress_id_7ee1008a_fk_user_address_id` FOREIGN KEY (`sellerAddress_id`) REFERENCES `user_address` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `resource_order_seller_id_ff847c14_fk_user_info_id` FOREIGN KEY (`seller_id`) REFERENCES `user_info` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for resource_product_type_one
-- ----------------------------
DROP TABLE IF EXISTS `resource_product_type_one`;
CREATE TABLE `resource_product_type_one`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_type` varchar(11) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `product_type`(`product_type`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for resource_product_type_three
-- ----------------------------
DROP TABLE IF EXISTS `resource_product_type_three`;
CREATE TABLE `resource_product_type_three`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_type` varchar(11) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `two_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `resource_product_typ_two_id_id_fe8f9f87_fk_resource_`(`two_id_id`) USING BTREE,
  CONSTRAINT `resource_product_typ_two_id_id_fe8f9f87_fk_resource_` FOREIGN KEY (`two_id_id`) REFERENCES `resource_product_type_two` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 230 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Records of resource_product_type_three
-- ----------------------------
INSERT INTO `resource_product_type_three` VALUES (7, 'WiFi放大器', 8);
INSERT INTO `resource_product_type_three` VALUES (8, '无线呼叫器', 8);
INSERT INTO `resource_product_type_three` VALUES (9, '格子间', 8);
INSERT INTO `resource_product_type_three` VALUES (10, '电脑桌', 8);
INSERT INTO `resource_product_type_three` VALUES (11, '办公椅', 8);
INSERT INTO `resource_product_type_three` VALUES (12, '理线器', 8);
INSERT INTO `resource_product_type_three` VALUES (13, '计算器', 8);
INSERT INTO `resource_product_type_three` VALUES (14, '荧光告示贴', 8);
INSERT INTO `resource_product_type_three` VALUES (15, '翻译笔', 8);
INSERT INTO `resource_product_type_three` VALUES (16, '毛笔', 8);
INSERT INTO `resource_product_type_three` VALUES (17, '马克笔', 8);
INSERT INTO `resource_product_type_three` VALUES (18, '文件收纳', 8);
INSERT INTO `resource_product_type_three` VALUES (19, '本册', 8);
INSERT INTO `resource_product_type_three` VALUES (20, '书写工具', 8);
INSERT INTO `resource_product_type_three` VALUES (21, '文具', 8);
INSERT INTO `resource_product_type_three` VALUES (22, '画具画材', 8);
INSERT INTO `resource_product_type_three` VALUES (23, '钢笔', 8);
INSERT INTO `resource_product_type_three` VALUES (24, '中性笔', 8);
INSERT INTO `resource_product_type_three` VALUES (25, '财会用品', 8);
INSERT INTO `resource_product_type_three` VALUES (26, '碎纸机', 8);
INSERT INTO `resource_product_type_three` VALUES (27, '包装设备', 8);
INSERT INTO `resource_product_type_three` VALUES (28, '定制T恤', 9);
INSERT INTO `resource_product_type_three` VALUES (29, '文化衫', 9);
INSERT INTO `resource_product_type_three` VALUES (30, '工作服', 9);
INSERT INTO `resource_product_type_three` VALUES (31, '卫衣定制', 9);
INSERT INTO `resource_product_type_three` VALUES (32, 'LOGO设计', 9);
INSERT INTO `resource_product_type_three` VALUES (33, 'VI设计', 9);
INSERT INTO `resource_product_type_three` VALUES (34, '海报定制', 9);
INSERT INTO `resource_product_type_three` VALUES (35, '3D效果图制作', 9);
INSERT INTO `resource_product_type_three` VALUES (36, '广告扇', 9);
INSERT INTO `resource_product_type_three` VALUES (37, '水晶奖杯', 9);
INSERT INTO `resource_product_type_three` VALUES (38, '胸牌工牌', 9);
INSERT INTO `resource_product_type_three` VALUES (39, '奖杯', 9);
INSERT INTO `resource_product_type_three` VALUES (40, '徽章', 9);
INSERT INTO `resource_product_type_three` VALUES (41, '洗照片', 9);
INSERT INTO `resource_product_type_three` VALUES (42, '照片冲印', 9);
INSERT INTO `resource_product_type_three` VALUES (43, '相册/照片书', 9);
INSERT INTO `resource_product_type_three` VALUES (44, '软陶人偶', 9);
INSERT INTO `resource_product_type_three` VALUES (45, '手绘漫画', 9);
INSERT INTO `resource_product_type_three` VALUES (46, '纸箱', 9);
INSERT INTO `resource_product_type_three` VALUES (47, '搬家纸箱', 9);
INSERT INTO `resource_product_type_three` VALUES (48, '胶带', 9);
INSERT INTO `resource_product_type_three` VALUES (49, '标签贴纸', 9);
INSERT INTO `resource_product_type_three` VALUES (50, '二维码贴纸', 9);
INSERT INTO `resource_product_type_three` VALUES (51, '塑料袋', 9);
INSERT INTO `resource_product_type_three` VALUES (52, '自封袋', 9);
INSERT INTO `resource_product_type_three` VALUES (53, '快递袋', 9);
INSERT INTO `resource_product_type_three` VALUES (54, '气泡膜', 9);
INSERT INTO `resource_product_type_three` VALUES (55, '编织袋', 9);
INSERT INTO `resource_product_type_three` VALUES (56, '飞机盒', 9);
INSERT INTO `resource_product_type_three` VALUES (57, '泡沫箱', 9);
INSERT INTO `resource_product_type_three` VALUES (58, '气柱袋', 9);
INSERT INTO `resource_product_type_three` VALUES (59, '纸手提袋', 9);
INSERT INTO `resource_product_type_three` VALUES (60, '打包绳带', 9);
INSERT INTO `resource_product_type_three` VALUES (61, '气泡信封', 9);
INSERT INTO `resource_product_type_three` VALUES (62, '缠绕膜', 9);
INSERT INTO `resource_product_type_three` VALUES (63, '物联网市场', 10);
INSERT INTO `resource_product_type_three` VALUES (64, '万用表', 10);
INSERT INTO `resource_product_type_three` VALUES (65, '电动螺丝刀', 10);
INSERT INTO `resource_product_type_three` VALUES (66, '管钳子', 10);
INSERT INTO `resource_product_type_three` VALUES (67, '电钻', 10);
INSERT INTO `resource_product_type_three` VALUES (68, '无尘锯', 10);
INSERT INTO `resource_product_type_three` VALUES (69, '电焊机', 10);
INSERT INTO `resource_product_type_three` VALUES (70, '角磨机', 10);
INSERT INTO `resource_product_type_three` VALUES (71, '切割机', 10);
INSERT INTO `resource_product_type_three` VALUES (72, '发电机', 10);
INSERT INTO `resource_product_type_three` VALUES (73, '快排阀', 10);
INSERT INTO `resource_product_type_three` VALUES (74, '增压泵', 10);
INSERT INTO `resource_product_type_three` VALUES (75, '钢珠', 10);
INSERT INTO `resource_product_type_three` VALUES (76, '测距仪', 10);
INSERT INTO `resource_product_type_three` VALUES (77, '水平仪', 10);
INSERT INTO `resource_product_type_three` VALUES (78, '传感器', 10);
INSERT INTO `resource_product_type_three` VALUES (79, '电容器', 10);
INSERT INTO `resource_product_type_three` VALUES (80, '变压器', 10);
INSERT INTO `resource_product_type_three` VALUES (81, '单片机开发板', 10);
INSERT INTO `resource_product_type_three` VALUES (82, '智能小车', 10);
INSERT INTO `resource_product_type_three` VALUES (83, '机器人套件', 10);
INSERT INTO `resource_product_type_three` VALUES (84, '3D打印耗材', 10);
INSERT INTO `resource_product_type_three` VALUES (85, 'GPS', 10);
INSERT INTO `resource_product_type_three` VALUES (86, '蓝牙', 10);
INSERT INTO `resource_product_type_three` VALUES (87, 'LED灯珠', 10);
INSERT INTO `resource_product_type_three` VALUES (88, '树莓派', 10);
INSERT INTO `resource_product_type_three` VALUES (89, '棉拖', 11);
INSERT INTO `resource_product_type_three` VALUES (90, '口罩', 11);
INSERT INTO `resource_product_type_three` VALUES (91, '足浴沐浴', 11);
INSERT INTO `resource_product_type_three` VALUES (92, '马桶套', 11);
INSERT INTO `resource_product_type_three` VALUES (93, '暖宝宝', 11);
INSERT INTO `resource_product_type_three` VALUES (94, '浴巾', 11);
INSERT INTO `resource_product_type_three` VALUES (95, '整理箱收纳盒', 11);
INSERT INTO `resource_product_type_three` VALUES (96, '雨伞', 11);
INSERT INTO `resource_product_type_three` VALUES (97, '暖宝', 11);
INSERT INTO `resource_product_type_three` VALUES (98, '热水袋', 11);
INSERT INTO `resource_product_type_three` VALUES (99, '梯子', 11);
INSERT INTO `resource_product_type_three` VALUES (100, '置物架', 11);
INSERT INTO `resource_product_type_three` VALUES (101, '拖把', 11);
INSERT INTO `resource_product_type_three` VALUES (102, '压缩袋', 11);
INSERT INTO `resource_product_type_three` VALUES (103, '收纳柜鞋柜', 11);
INSERT INTO `resource_product_type_three` VALUES (104, '桌面收纳', 11);
INSERT INTO `resource_product_type_three` VALUES (105, '衣物洗晒', 11);
INSERT INTO `resource_product_type_three` VALUES (106, '衣物粘尘', 11);
INSERT INTO `resource_product_type_three` VALUES (107, '垃圾桶', 11);
INSERT INTO `resource_product_type_three` VALUES (108, '刷牙洗脸', 11);
INSERT INTO `resource_product_type_three` VALUES (109, '梳子镜子', 11);
INSERT INTO `resource_product_type_three` VALUES (110, '干发帽', 11);
INSERT INTO `resource_product_type_three` VALUES (111, '圣诞品', 11);
INSERT INTO `resource_product_type_three` VALUES (112, '礼品', 11);
INSERT INTO `resource_product_type_three` VALUES (113, '婚房布置', 11);
INSERT INTO `resource_product_type_three` VALUES (114, '喜糖盒', 11);
INSERT INTO `resource_product_type_three` VALUES (115, '保温杯', 12);
INSERT INTO `resource_product_type_three` VALUES (116, '保温壶', 12);
INSERT INTO `resource_product_type_three` VALUES (117, '焖烧罐', 12);
INSERT INTO `resource_product_type_three` VALUES (118, '储物罐', 12);
INSERT INTO `resource_product_type_three` VALUES (119, '烧烤炉', 12);
INSERT INTO `resource_product_type_three` VALUES (120, '刀具套组', 12);
INSERT INTO `resource_product_type_three` VALUES (121, '砂锅', 12);
INSERT INTO `resource_product_type_three` VALUES (122, '炒锅', 12);
INSERT INTO `resource_product_type_three` VALUES (123, '铸铁锅', 12);
INSERT INTO `resource_product_type_three` VALUES (124, '汤锅煲', 12);
INSERT INTO `resource_product_type_three` VALUES (125, '烘焙', 12);
INSERT INTO `resource_product_type_three` VALUES (126, '调味瓶罐', 12);
INSERT INTO `resource_product_type_three` VALUES (127, '厨房小工具', 12);
INSERT INTO `resource_product_type_three` VALUES (128, '厨房置物架', 12);
INSERT INTO `resource_product_type_three` VALUES (129, '压力锅', 12);
INSERT INTO `resource_product_type_three` VALUES (130, '餐具套装', 12);
INSERT INTO `resource_product_type_three` VALUES (131, '碗', 12);
INSERT INTO `resource_product_type_three` VALUES (132, '餐盘', 12);
INSERT INTO `resource_product_type_three` VALUES (133, '茶壶', 12);
INSERT INTO `resource_product_type_three` VALUES (134, '茶杯', 12);
INSERT INTO `resource_product_type_three` VALUES (135, '茶具套装', 12);
INSERT INTO `resource_product_type_three` VALUES (136, '玻璃杯', 12);
INSERT INTO `resource_product_type_three` VALUES (137, '饭盒', 12);
INSERT INTO `resource_product_type_three` VALUES (138, '紫砂壶', 12);
INSERT INTO `resource_product_type_three` VALUES (139, '手套抹布', 12);
INSERT INTO `resource_product_type_three` VALUES (140, '围裙', 12);
INSERT INTO `resource_product_type_three` VALUES (141, '洗碗巾', 12);
INSERT INTO `resource_product_type_three` VALUES (142, '垃圾袋', 12);
INSERT INTO `resource_product_type_three` VALUES (143, '厨房用刷', 12);
INSERT INTO `resource_product_type_three` VALUES (144, '创可贴', 13);
INSERT INTO `resource_product_type_three` VALUES (145, '消毒用品', 13);
INSERT INTO `resource_product_type_three` VALUES (146, '体温计', 13);
INSERT INTO `resource_product_type_three` VALUES (147, '冷敷降温', 13);
INSERT INTO `resource_product_type_three` VALUES (148, '急救箱', 13);
INSERT INTO `resource_product_type_three` VALUES (149, '医用口罩', 13);
INSERT INTO `resource_product_type_three` VALUES (150, '绷带纱布', 13);
INSERT INTO `resource_product_type_three` VALUES (151, '血压监测', 13);
INSERT INTO `resource_product_type_three` VALUES (152, '血糖监测', 13);
INSERT INTO `resource_product_type_three` VALUES (153, '心率监测', 13);
INSERT INTO `resource_product_type_three` VALUES (154, '呼吸制氧', 13);
INSERT INTO `resource_product_type_three` VALUES (155, '拐杖', 13);
INSERT INTO `resource_product_type_three` VALUES (156, '轮椅', 13);
INSERT INTO `resource_product_type_three` VALUES (157, '助行器', 13);
INSERT INTO `resource_product_type_three` VALUES (158, '矫正牵引', 13);
INSERT INTO `resource_product_type_three` VALUES (159, '医用床上护理', 13);
INSERT INTO `resource_product_type_three` VALUES (160, '拔罐', 13);
INSERT INTO `resource_product_type_three` VALUES (161, '英语四级', 14);
INSERT INTO `resource_product_type_three` VALUES (162, '2018考研', 14);
INSERT INTO `resource_product_type_three` VALUES (163, '成人学历', 14);
INSERT INTO `resource_product_type_three` VALUES (164, '小学教学', 14);
INSERT INTO `resource_product_type_three` VALUES (165, '雅思托福', 14);
INSERT INTO `resource_product_type_three` VALUES (166, '学历提升', 14);
INSERT INTO `resource_product_type_three` VALUES (167, '会计提升', 14);
INSERT INTO `resource_product_type_three` VALUES (168, 'ps美工技能', 14);
INSERT INTO `resource_product_type_three` VALUES (169, '考研辅导', 14);
INSERT INTO `resource_product_type_three` VALUES (170, '外教口语课', 14);
INSERT INTO `resource_product_type_three` VALUES (171, '建造师', 14);
INSERT INTO `resource_product_type_three` VALUES (172, '口语一对一', 14);
INSERT INTO `resource_product_type_three` VALUES (173, '驾照报名', 14);
INSERT INTO `resource_product_type_three` VALUES (174, '汽车维修', 14);
INSERT INTO `resource_product_type_three` VALUES (175, '化妆课程', 14);
INSERT INTO `resource_product_type_three` VALUES (176, '电商培训', 14);
INSERT INTO `resource_product_type_three` VALUES (177, '少儿英语', 14);
INSERT INTO `resource_product_type_three` VALUES (178, '公务员考试', 14);
INSERT INTO `resource_product_type_three` VALUES (179, '中小学辅导', 14);
INSERT INTO `resource_product_type_three` VALUES (180, '宝宝早教', 14);
INSERT INTO `resource_product_type_three` VALUES (181, '健身减肥', 14);
INSERT INTO `resource_product_type_three` VALUES (182, 'DIY手工', 14);
INSERT INTO `resource_product_type_three` VALUES (183, '微信小程序', 14);
INSERT INTO `resource_product_type_three` VALUES (184, 'JAVA', 14);
INSERT INTO `resource_product_type_three` VALUES (185, 'CAD教程', 14);
INSERT INTO `resource_product_type_three` VALUES (186, '驾校学车', 14);
INSERT INTO `resource_product_type_three` VALUES (187, '劳动节福利', 15);
INSERT INTO `resource_product_type_three` VALUES (188, '超市卡', 15);
INSERT INTO `resource_product_type_three` VALUES (189, '沃尔玛', 15);
INSERT INTO `resource_product_type_three` VALUES (190, '家乐福', 15);
INSERT INTO `resource_product_type_three` VALUES (191, '银泰卡', 15);
INSERT INTO `resource_product_type_three` VALUES (192, '面包券', 15);
INSERT INTO `resource_product_type_three` VALUES (193, '来伊份券', 15);
INSERT INTO `resource_product_type_three` VALUES (194, '粽子券', 15);
INSERT INTO `resource_product_type_three` VALUES (195, '熟食/半成品', 15);
INSERT INTO `resource_product_type_three` VALUES (196, '星巴克', 15);
INSERT INTO `resource_product_type_three` VALUES (197, '咖啡', 15);
INSERT INTO `resource_product_type_three` VALUES (198, '哈根达斯', 15);
INSERT INTO `resource_product_type_three` VALUES (199, '冰淇淋', 15);
INSERT INTO `resource_product_type_three` VALUES (200, '网站建设', 15);
INSERT INTO `resource_product_type_three` VALUES (201, '云服务器', 15);
INSERT INTO `resource_product_type_three` VALUES (202, '财务管理', 15);
INSERT INTO `resource_product_type_three` VALUES (203, '网页设计', 15);
INSERT INTO `resource_product_type_three` VALUES (204, '软件', 15);
INSERT INTO `resource_product_type_three` VALUES (205, '婚纱摄影', 16);
INSERT INTO `resource_product_type_three` VALUES (206, '青岛婚拍', 16);
INSERT INTO `resource_product_type_three` VALUES (207, '丽江婚拍', 16);
INSERT INTO `resource_product_type_three` VALUES (208, '三亚婚拍', 16);
INSERT INTO `resource_product_type_three` VALUES (209, '厦门婚拍', 16);
INSERT INTO `resource_product_type_three` VALUES (210, '新娘跟妆', 16);
INSERT INTO `resource_product_type_three` VALUES (211, '婚礼司仪', 16);
INSERT INTO `resource_product_type_three` VALUES (212, '婚车租赁', 16);
INSERT INTO `resource_product_type_three` VALUES (213, '婚礼策划', 16);
INSERT INTO `resource_product_type_three` VALUES (214, '婚宴预订', 16);
INSERT INTO `resource_product_type_three` VALUES (215, '婚纱礼服', 16);
INSERT INTO `resource_product_type_three` VALUES (216, '礼服租赁', 16);
INSERT INTO `resource_product_type_three` VALUES (217, '家电清洗', 16);
INSERT INTO `resource_product_type_three` VALUES (218, '家庭保洁', 16);
INSERT INTO `resource_product_type_three` VALUES (219, '搬家搬运', 16);
INSERT INTO `resource_product_type_three` VALUES (220, '在线洗衣', 16);
INSERT INTO `resource_product_type_three` VALUES (221, '上门养车', 16);
INSERT INTO `resource_product_type_three` VALUES (222, '跑腿代办', 16);
INSERT INTO `resource_product_type_three` VALUES (223, '名企招聘', 16);
INSERT INTO `resource_product_type_three` VALUES (224, '上门美甲', 16);
INSERT INTO `resource_product_type_three` VALUES (225, '入职体检', 16);
INSERT INTO `resource_product_type_three` VALUES (226, '法律咨询', 16);
INSERT INTO `resource_product_type_three` VALUES (227, '上门按摩', 16);
INSERT INTO `resource_product_type_three` VALUES (228, '专业翻译', 16);
INSERT INTO `resource_product_type_three` VALUES (229, '其它', 17);

-- ----------------------------
-- Table structure for resource_product_type_two
-- ----------------------------
DROP TABLE IF EXISTS `resource_product_type_two`;
CREATE TABLE `resource_product_type_two`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_type` varchar(11) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `one_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `resource_product_typ_one_id_id_4b4882ba_fk_resource_`(`one_id_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 18 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Records of resource_product_type_two
-- ----------------------------
INSERT INTO `resource_product_type_two` VALUES (8, '办公', 0);
INSERT INTO `resource_product_type_two` VALUES (9, 'DIY', 0);
INSERT INTO `resource_product_type_two` VALUES (10, '五金电子', 0);
INSERT INTO `resource_product_type_two` VALUES (11, '百货', 0);
INSERT INTO `resource_product_type_two` VALUES (12, '餐厨', 0);
INSERT INTO `resource_product_type_two` VALUES (13, '家庭保健', 0);
INSERT INTO `resource_product_type_two` VALUES (14, '学习', 0);
INSERT INTO `resource_product_type_two` VALUES (15, '卡券', 0);
INSERT INTO `resource_product_type_two` VALUES (16, '本地服务', 0);
INSERT INTO `resource_product_type_two` VALUES (17, '其他', 0);

-- ----------------------------
-- Table structure for resource_products
-- ----------------------------
DROP TABLE IF EXISTS `resource_products`;
CREATE TABLE `resource_products`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(15) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `price` double NOT NULL,
  `category` int(11) NOT NULL,
  `title` varchar(50) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `pnum` int(11) NOT NULL,
  `imgurl` varchar(256) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `description` varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `upload_time` datetime(6) DEFAULT NULL,
  `status` varchar(2) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `product_type_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `resource_products_product_type_id_4bb7054e_fk_resource_`(`product_type_id`) USING BTREE,
  INDEX `resource_products_user_id_cd0b97ec_fk_user_info_id`(`user_id`) USING BTREE,
  CONSTRAINT `resource_products_product_type_id_4bb7054e_fk_resource_` FOREIGN KEY (`product_type_id`) REFERENCES `resource_product_type_three` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `resource_products_user_id_cd0b97ec_fk_user_info_id` FOREIGN KEY (`user_id`) REFERENCES `user_info` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Records of resource_products
-- ----------------------------
INSERT INTO `resource_products` VALUES (6, '手机', 1000, 10, '手机', 0, '9b3536a3-df1f-4ef9-9030-0cf25cb27ec5.jfif', '这是一个商品', '2019-04-15 23:13:56.463085', '0', 229, 1);

-- ----------------------------
-- Table structure for resource_status
-- ----------------------------
DROP TABLE IF EXISTS `resource_status`;
CREATE TABLE `resource_status`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `guaranty` int(11) NOT NULL,
  `statusName` varchar(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for resource_user_collect
-- ----------------------------
DROP TABLE IF EXISTS `resource_user_collect`;
CREATE TABLE `resource_user_collect`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `collect_resource_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `resource_user_collect_user_id_collect_resource_id_9ede3665_uniq`(`user_id`, `collect_resource_id`) USING BTREE,
  INDEX `resource_user_collec_collect_resource_id_53a88cb8_fk_resource_`(`collect_resource_id`) USING BTREE,
  CONSTRAINT `resource_user_collec_collect_resource_id_53a88cb8_fk_resource_` FOREIGN KEY (`collect_resource_id`) REFERENCES `resource_products` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `resource_user_collect_user_id_cc105b27_fk_user_info_id` FOREIGN KEY (`user_id`) REFERENCES `user_info` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for user_address
-- ----------------------------
DROP TABLE IF EXISTS `user_address`;
CREATE TABLE `user_address`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `concact_name` varchar(10) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `concact_telephone` varchar(11) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `detailed_address` varchar(100) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `default` int(11) NOT NULL,
  `city_id` int(11) NOT NULL,
  `provice_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `user_address_city_id_654faf8b_fk_user_city_id`(`city_id`) USING BTREE,
  INDEX `user_address_provice_id_2b1d9584_fk_user_province_id`(`provice_id`) USING BTREE,
  INDEX `user_address_user_id_64deb2c7_fk_user_user_id`(`user_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Records of user_address
-- ----------------------------
INSERT INTO `user_address` VALUES (1, '饶宝仕', '15755642351', NULL, 1, 1, 1, 1);

-- ----------------------------
-- Table structure for user_adminmsg
-- ----------------------------
DROP TABLE IF EXISTS `user_adminmsg`;
CREATE TABLE `user_adminmsg`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `msg` varchar(256) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `msg_time` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `user_adminmsg_user_id_78747ea8_fk_user_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `user_adminmsg_user_id_78747ea8_fk_user_user_id` FOREIGN KEY (`user_id`) REFERENCES `user_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for user_city
-- ----------------------------
DROP TABLE IF EXISTS `user_city`;
CREATE TABLE `user_city`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `city_name` varchar(10) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `c_p_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `user_city_c_p_id_02bdebe2_fk_user_province_id`(`c_p_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 392 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Records of user_city
-- ----------------------------
INSERT INTO `user_city` VALUES (1, '北京市', 1);
INSERT INTO `user_city` VALUES (2, '天津市', 2);
INSERT INTO `user_city` VALUES (3, '石家庄市', 3);
INSERT INTO `user_city` VALUES (4, '唐山市', 3);
INSERT INTO `user_city` VALUES (5, '秦皇岛市', 4);
INSERT INTO `user_city` VALUES (6, '邯郸市', 5);
INSERT INTO `user_city` VALUES (7, '邢台市', 6);
INSERT INTO `user_city` VALUES (8, '保定市', 7);
INSERT INTO `user_city` VALUES (9, '张家口', 8);
INSERT INTO `user_city` VALUES (10, '承德市', 9);
INSERT INTO `user_city` VALUES (11, '沧州市', 10);
INSERT INTO `user_city` VALUES (12, '廊坊市', 11);
INSERT INTO `user_city` VALUES (13, '衡水市', 12);
INSERT INTO `user_city` VALUES (14, '太原市', 4);
INSERT INTO `user_city` VALUES (15, '大同市', 14);
INSERT INTO `user_city` VALUES (16, '阳泉市', 15);
INSERT INTO `user_city` VALUES (17, '长治市', 16);
INSERT INTO `user_city` VALUES (18, '晋城市', 17);
INSERT INTO `user_city` VALUES (19, '朔州市', 18);
INSERT INTO `user_city` VALUES (20, '忻州市', 19);
INSERT INTO `user_city` VALUES (21, '吕梁市', 20);
INSERT INTO `user_city` VALUES (22, '晋中市', 21);
INSERT INTO `user_city` VALUES (23, '临汾市', 22);
INSERT INTO `user_city` VALUES (24, '运城市', 23);
INSERT INTO `user_city` VALUES (25, '呼和浩特市', 5);
INSERT INTO `user_city` VALUES (26, '包头市', 25);
INSERT INTO `user_city` VALUES (27, '乌海市', 26);
INSERT INTO `user_city` VALUES (28, '赤峰市', 27);
INSERT INTO `user_city` VALUES (29, '呼伦贝尔市', 28);
INSERT INTO `user_city` VALUES (30, '兴安盟', 29);
INSERT INTO `user_city` VALUES (31, '通辽市', 30);
INSERT INTO `user_city` VALUES (32, '锡林郭勒盟', 31);
INSERT INTO `user_city` VALUES (33, '乌兰察布盟', 32);
INSERT INTO `user_city` VALUES (34, '伊克昭盟', 33);
INSERT INTO `user_city` VALUES (35, '巴彦淖尔盟', 34);
INSERT INTO `user_city` VALUES (36, '阿拉善盟', 35);
INSERT INTO `user_city` VALUES (37, '沈阳市', 6);
INSERT INTO `user_city` VALUES (38, '大连市', 37);
INSERT INTO `user_city` VALUES (39, '鞍山市', 38);
INSERT INTO `user_city` VALUES (40, '抚顺市', 39);
INSERT INTO `user_city` VALUES (41, '本溪市', 40);
INSERT INTO `user_city` VALUES (42, '丹东市', 41);
INSERT INTO `user_city` VALUES (43, '锦州市', 42);
INSERT INTO `user_city` VALUES (44, '营口市', 43);
INSERT INTO `user_city` VALUES (45, '阜新市', 44);
INSERT INTO `user_city` VALUES (46, '辽阳市', 45);
INSERT INTO `user_city` VALUES (47, '盘锦', 46);
INSERT INTO `user_city` VALUES (48, '铁岭市', 47);
INSERT INTO `user_city` VALUES (49, '朝阳市', 48);
INSERT INTO `user_city` VALUES (50, '葫芦岛市', 49);
INSERT INTO `user_city` VALUES (51, '其他', 50);
INSERT INTO `user_city` VALUES (52, '长春市', 7);
INSERT INTO `user_city` VALUES (53, '吉林市', 52);
INSERT INTO `user_city` VALUES (54, '四平', 53);
INSERT INTO `user_city` VALUES (55, '辽源市', 54);
INSERT INTO `user_city` VALUES (56, '通化市', 55);
INSERT INTO `user_city` VALUES (57, '白山市', 56);
INSERT INTO `user_city` VALUES (58, '松原市', 57);
INSERT INTO `user_city` VALUES (59, '白城市', 58);
INSERT INTO `user_city` VALUES (60, '延边朝鲜族自治州', 59);
INSERT INTO `user_city` VALUES (61, '其他', 60);
INSERT INTO `user_city` VALUES (62, '哈尔滨市', 8);
INSERT INTO `user_city` VALUES (63, '齐齐哈尔市', 62);
INSERT INTO `user_city` VALUES (64, '鹤岗市', 63);
INSERT INTO `user_city` VALUES (65, '双鸭山', 64);
INSERT INTO `user_city` VALUES (66, '鸡西市', 65);
INSERT INTO `user_city` VALUES (67, '大庆市', 66);
INSERT INTO `user_city` VALUES (68, '伊春市', 67);
INSERT INTO `user_city` VALUES (69, '牡丹江市', 68);
INSERT INTO `user_city` VALUES (70, '佳木斯市', 69);
INSERT INTO `user_city` VALUES (71, '七台河市', 70);
INSERT INTO `user_city` VALUES (72, '黑河市', 71);
INSERT INTO `user_city` VALUES (73, '绥化市', 72);
INSERT INTO `user_city` VALUES (74, '大兴安岭地区', 73);
INSERT INTO `user_city` VALUES (75, '其他', 74);
INSERT INTO `user_city` VALUES (76, '上海市', 9);
INSERT INTO `user_city` VALUES (77, '南京市', 10);
INSERT INTO `user_city` VALUES (78, '苏州市', 77);
INSERT INTO `user_city` VALUES (79, '无锡市', 78);
INSERT INTO `user_city` VALUES (80, '常州市', 79);
INSERT INTO `user_city` VALUES (81, '镇江市', 80);
INSERT INTO `user_city` VALUES (82, '南通市', 81);
INSERT INTO `user_city` VALUES (83, '泰州市', 82);
INSERT INTO `user_city` VALUES (84, '扬州市', 83);
INSERT INTO `user_city` VALUES (85, '盐城市', 84);
INSERT INTO `user_city` VALUES (86, '连云港市', 85);
INSERT INTO `user_city` VALUES (87, '徐州市', 86);
INSERT INTO `user_city` VALUES (88, '淮安市', 87);
INSERT INTO `user_city` VALUES (89, '宿迁市', 88);
INSERT INTO `user_city` VALUES (90, '其他', 89);
INSERT INTO `user_city` VALUES (91, '杭州市', 11);
INSERT INTO `user_city` VALUES (92, '宁波市', 91);
INSERT INTO `user_city` VALUES (93, '温州市', 92);
INSERT INTO `user_city` VALUES (94, '嘉兴市', 93);
INSERT INTO `user_city` VALUES (95, '湖州市', 94);
INSERT INTO `user_city` VALUES (96, '绍兴市', 95);
INSERT INTO `user_city` VALUES (97, '金华市', 96);
INSERT INTO `user_city` VALUES (98, '衢州市', 97);
INSERT INTO `user_city` VALUES (99, '舟山市', 98);
INSERT INTO `user_city` VALUES (100, '台州市', 99);
INSERT INTO `user_city` VALUES (101, '丽水市', 100);
INSERT INTO `user_city` VALUES (102, '其他市', 101);
INSERT INTO `user_city` VALUES (103, '合肥市', 12);
INSERT INTO `user_city` VALUES (104, '芜湖市', 103);
INSERT INTO `user_city` VALUES (105, '蚌埠市', 104);
INSERT INTO `user_city` VALUES (106, '淮南市', 105);
INSERT INTO `user_city` VALUES (107, '马鞍山市', 106);
INSERT INTO `user_city` VALUES (108, '淮北市', 107);
INSERT INTO `user_city` VALUES (109, '铜陵市', 108);
INSERT INTO `user_city` VALUES (110, '安庆市', 109);
INSERT INTO `user_city` VALUES (111, '黄山市', 110);
INSERT INTO `user_city` VALUES (112, '滁州市', 111);
INSERT INTO `user_city` VALUES (113, '阜阳市', 112);
INSERT INTO `user_city` VALUES (114, '宿州市', 113);
INSERT INTO `user_city` VALUES (115, '巢湖市', 114);
INSERT INTO `user_city` VALUES (116, '六安市', 115);
INSERT INTO `user_city` VALUES (117, '亳州市', 116);
INSERT INTO `user_city` VALUES (118, '池州市', 117);
INSERT INTO `user_city` VALUES (119, '宣城市', 118);
INSERT INTO `user_city` VALUES (120, '其他市', 119);
INSERT INTO `user_city` VALUES (121, '福州市', 13);
INSERT INTO `user_city` VALUES (122, '厦门市', 121);
INSERT INTO `user_city` VALUES (123, '莆田市', 122);
INSERT INTO `user_city` VALUES (124, '三明市', 123);
INSERT INTO `user_city` VALUES (125, '泉州市', 124);
INSERT INTO `user_city` VALUES (126, '漳州市', 125);
INSERT INTO `user_city` VALUES (127, '南平市', 126);
INSERT INTO `user_city` VALUES (128, '龙岩市', 127);
INSERT INTO `user_city` VALUES (129, '宁德市', 128);
INSERT INTO `user_city` VALUES (130, '其他', 129);
INSERT INTO `user_city` VALUES (131, '南昌市', 14);
INSERT INTO `user_city` VALUES (132, '景德镇市', 131);
INSERT INTO `user_city` VALUES (133, '萍乡市', 132);
INSERT INTO `user_city` VALUES (134, '九江市', 133);
INSERT INTO `user_city` VALUES (135, '新余市', 134);
INSERT INTO `user_city` VALUES (136, '鹰潭市', 135);
INSERT INTO `user_city` VALUES (137, '赣州市', 136);
INSERT INTO `user_city` VALUES (138, '吉安市', 137);
INSERT INTO `user_city` VALUES (139, '宜春市', 138);
INSERT INTO `user_city` VALUES (140, '抚州市', 139);
INSERT INTO `user_city` VALUES (141, '上饶市', 140);
INSERT INTO `user_city` VALUES (142, '其他', 141);
INSERT INTO `user_city` VALUES (143, '济南市', 15);
INSERT INTO `user_city` VALUES (144, '青岛市', 143);
INSERT INTO `user_city` VALUES (145, '淄博市', 144);
INSERT INTO `user_city` VALUES (146, '枣庄市', 145);
INSERT INTO `user_city` VALUES (147, '东营市', 146);
INSERT INTO `user_city` VALUES (148, '烟台市', 147);
INSERT INTO `user_city` VALUES (149, '潍坊市', 148);
INSERT INTO `user_city` VALUES (150, '济宁市', 149);
INSERT INTO `user_city` VALUES (151, '泰安市', 150);
INSERT INTO `user_city` VALUES (152, '威海市', 151);
INSERT INTO `user_city` VALUES (153, '日照市', 152);
INSERT INTO `user_city` VALUES (154, '莱芜市', 153);
INSERT INTO `user_city` VALUES (155, '临沂市', 154);
INSERT INTO `user_city` VALUES (156, '德州市', 155);
INSERT INTO `user_city` VALUES (157, '聊城市', 156);
INSERT INTO `user_city` VALUES (158, '滨州市', 157);
INSERT INTO `user_city` VALUES (159, '菏泽市', 158);
INSERT INTO `user_city` VALUES (160, '其他', 159);
INSERT INTO `user_city` VALUES (161, '郑州市', 16);
INSERT INTO `user_city` VALUES (162, '开封市', 161);
INSERT INTO `user_city` VALUES (163, '洛阳市', 162);
INSERT INTO `user_city` VALUES (164, '平顶山市', 163);
INSERT INTO `user_city` VALUES (165, '安阳市', 164);
INSERT INTO `user_city` VALUES (166, '鹤壁市', 165);
INSERT INTO `user_city` VALUES (167, '新乡市', 166);
INSERT INTO `user_city` VALUES (168, '焦作市', 167);
INSERT INTO `user_city` VALUES (169, '濮阳市', 168);
INSERT INTO `user_city` VALUES (170, '许昌市', 169);
INSERT INTO `user_city` VALUES (171, '漯河市', 170);
INSERT INTO `user_city` VALUES (172, '三门峡市', 171);
INSERT INTO `user_city` VALUES (173, '南阳市', 172);
INSERT INTO `user_city` VALUES (174, '商丘市', 173);
INSERT INTO `user_city` VALUES (175, '信阳市', 174);
INSERT INTO `user_city` VALUES (176, '周口市', 175);
INSERT INTO `user_city` VALUES (177, '驻马店市', 176);
INSERT INTO `user_city` VALUES (178, '焦作市', 177);
INSERT INTO `user_city` VALUES (179, '其他', 178);
INSERT INTO `user_city` VALUES (180, '武汉市', 17);
INSERT INTO `user_city` VALUES (181, '黄石市', 180);
INSERT INTO `user_city` VALUES (182, '十堰市', 181);
INSERT INTO `user_city` VALUES (183, '荆州市', 182);
INSERT INTO `user_city` VALUES (184, '宜昌市', 183);
INSERT INTO `user_city` VALUES (185, '襄樊市', 184);
INSERT INTO `user_city` VALUES (186, '鄂州市', 185);
INSERT INTO `user_city` VALUES (187, '荆门市', 186);
INSERT INTO `user_city` VALUES (188, '孝感市', 187);
INSERT INTO `user_city` VALUES (189, '黄冈市', 188);
INSERT INTO `user_city` VALUES (190, '咸宁市', 189);
INSERT INTO `user_city` VALUES (191, '随州市', 190);
INSERT INTO `user_city` VALUES (192, '恩施土家族苗族自治州', 191);
INSERT INTO `user_city` VALUES (193, '仙桃市', 192);
INSERT INTO `user_city` VALUES (194, '天门市', 193);
INSERT INTO `user_city` VALUES (195, '潜江市', 194);
INSERT INTO `user_city` VALUES (196, '神农架林区', 195);
INSERT INTO `user_city` VALUES (197, '其他', 196);
INSERT INTO `user_city` VALUES (198, '长沙市', 18);
INSERT INTO `user_city` VALUES (199, '株洲市', 198);
INSERT INTO `user_city` VALUES (200, '湘潭市', 199);
INSERT INTO `user_city` VALUES (201, '衡阳市', 200);
INSERT INTO `user_city` VALUES (202, '邵阳市', 201);
INSERT INTO `user_city` VALUES (203, '岳阳市', 202);
INSERT INTO `user_city` VALUES (204, '常德市', 203);
INSERT INTO `user_city` VALUES (205, '张家界市', 204);
INSERT INTO `user_city` VALUES (206, '益阳市', 205);
INSERT INTO `user_city` VALUES (207, '郴州市', 206);
INSERT INTO `user_city` VALUES (208, '永州市', 207);
INSERT INTO `user_city` VALUES (209, '怀化市', 208);
INSERT INTO `user_city` VALUES (210, '娄底市', 209);
INSERT INTO `user_city` VALUES (211, '湘西土家族苗族自治州', 210);
INSERT INTO `user_city` VALUES (212, '其他', 211);
INSERT INTO `user_city` VALUES (213, '广州市', 19);
INSERT INTO `user_city` VALUES (214, '深圳市', 213);
INSERT INTO `user_city` VALUES (215, '东莞市', 214);
INSERT INTO `user_city` VALUES (216, '中山市', 215);
INSERT INTO `user_city` VALUES (217, '潮州市', 216);
INSERT INTO `user_city` VALUES (218, '揭阳市', 217);
INSERT INTO `user_city` VALUES (219, '云浮市', 218);
INSERT INTO `user_city` VALUES (220, '珠海市', 219);
INSERT INTO `user_city` VALUES (221, '汕头市', 220);
INSERT INTO `user_city` VALUES (222, '韶关市', 221);
INSERT INTO `user_city` VALUES (223, '佛山市', 222);
INSERT INTO `user_city` VALUES (224, '江门市', 223);
INSERT INTO `user_city` VALUES (225, '湛江市', 224);
INSERT INTO `user_city` VALUES (226, '茂名市', 225);
INSERT INTO `user_city` VALUES (227, '肇庆市', 226);
INSERT INTO `user_city` VALUES (228, '惠州市', 227);
INSERT INTO `user_city` VALUES (229, '梅州市', 228);
INSERT INTO `user_city` VALUES (230, '汕尾市', 229);
INSERT INTO `user_city` VALUES (231, '河源市', 230);
INSERT INTO `user_city` VALUES (232, '阳江市', 231);
INSERT INTO `user_city` VALUES (233, '清远市', 232);
INSERT INTO `user_city` VALUES (234, '南宁市', 20);
INSERT INTO `user_city` VALUES (235, '柳州市', 234);
INSERT INTO `user_city` VALUES (236, '桂林市', 235);
INSERT INTO `user_city` VALUES (237, '梧州市', 236);
INSERT INTO `user_city` VALUES (238, '北海市', 237);
INSERT INTO `user_city` VALUES (239, '防城港市', 238);
INSERT INTO `user_city` VALUES (240, '钦州市', 239);
INSERT INTO `user_city` VALUES (241, '贵港市', 240);
INSERT INTO `user_city` VALUES (242, '玉林市', 241);
INSERT INTO `user_city` VALUES (243, '百色市', 242);
INSERT INTO `user_city` VALUES (244, '贺州市', 243);
INSERT INTO `user_city` VALUES (245, '河池市', 244);
INSERT INTO `user_city` VALUES (246, '来宾市', 245);
INSERT INTO `user_city` VALUES (247, '崇左市', 246);
INSERT INTO `user_city` VALUES (248, '其他市', 247);
INSERT INTO `user_city` VALUES (249, '海口市', 21);
INSERT INTO `user_city` VALUES (250, '三亚市', 249);
INSERT INTO `user_city` VALUES (251, '五指山市', 250);
INSERT INTO `user_city` VALUES (252, '琼海市', 251);
INSERT INTO `user_city` VALUES (253, '儋州市', 252);
INSERT INTO `user_city` VALUES (254, '文昌市', 253);
INSERT INTO `user_city` VALUES (255, '万宁市', 254);
INSERT INTO `user_city` VALUES (256, '东方市', 255);
INSERT INTO `user_city` VALUES (257, '澄迈县', 256);
INSERT INTO `user_city` VALUES (258, '定安县', 257);
INSERT INTO `user_city` VALUES (259, '屯昌县', 258);
INSERT INTO `user_city` VALUES (260, '临高县', 259);
INSERT INTO `user_city` VALUES (261, '白沙黎族自治县', 260);
INSERT INTO `user_city` VALUES (262, '昌江黎族自治县', 261);
INSERT INTO `user_city` VALUES (263, '乐东黎族自治县', 262);
INSERT INTO `user_city` VALUES (264, '陵水黎族自治县', 263);
INSERT INTO `user_city` VALUES (265, '保亭黎族苗族自治县', 264);
INSERT INTO `user_city` VALUES (266, '琼中黎族苗族自治县', 265);
INSERT INTO `user_city` VALUES (267, '其他', 266);
INSERT INTO `user_city` VALUES (268, '重庆市', 22);
INSERT INTO `user_city` VALUES (269, '成都市', 23);
INSERT INTO `user_city` VALUES (270, '自贡市', 269);
INSERT INTO `user_city` VALUES (271, '攀枝花市', 270);
INSERT INTO `user_city` VALUES (272, '泸州市', 271);
INSERT INTO `user_city` VALUES (273, '德阳市', 272);
INSERT INTO `user_city` VALUES (274, '绵阳市', 273);
INSERT INTO `user_city` VALUES (275, '广元市', 274);
INSERT INTO `user_city` VALUES (276, '遂宁市', 275);
INSERT INTO `user_city` VALUES (277, '内江市', 276);
INSERT INTO `user_city` VALUES (278, '乐山市', 277);
INSERT INTO `user_city` VALUES (279, '南充', 278);
INSERT INTO `user_city` VALUES (280, '眉山市', 279);
INSERT INTO `user_city` VALUES (281, '宜宾市', 280);
INSERT INTO `user_city` VALUES (282, '广安市', 281);
INSERT INTO `user_city` VALUES (283, '达州市', 282);
INSERT INTO `user_city` VALUES (284, '雅安市', 283);
INSERT INTO `user_city` VALUES (285, '巴中市', 284);
INSERT INTO `user_city` VALUES (286, '资阳市', 285);
INSERT INTO `user_city` VALUES (287, '阿坝藏族羌族自治州', 286);
INSERT INTO `user_city` VALUES (288, '甘孜藏族自治州', 287);
INSERT INTO `user_city` VALUES (289, '凉山彝族自治州', 288);
INSERT INTO `user_city` VALUES (290, '其他', 289);
INSERT INTO `user_city` VALUES (291, '贵阳市', 24);
INSERT INTO `user_city` VALUES (292, '六盘水市', 291);
INSERT INTO `user_city` VALUES (293, '遵义市', 292);
INSERT INTO `user_city` VALUES (294, '安顺市', 293);
INSERT INTO `user_city` VALUES (295, '铜仁地区', 294);
INSERT INTO `user_city` VALUES (296, '毕节地区', 295);
INSERT INTO `user_city` VALUES (297, '黔西南布依族苗族自治', 296);
INSERT INTO `user_city` VALUES (298, '黔东南苗族侗族自治州', 297);
INSERT INTO `user_city` VALUES (299, '黔南布依族苗族自治州', 298);
INSERT INTO `user_city` VALUES (300, '其他', 299);
INSERT INTO `user_city` VALUES (301, '昆明市', 25);
INSERT INTO `user_city` VALUES (302, '曲靖市', 301);
INSERT INTO `user_city` VALUES (303, '玉溪市', 302);
INSERT INTO `user_city` VALUES (304, '保山市', 303);
INSERT INTO `user_city` VALUES (305, '昭通市', 304);
INSERT INTO `user_city` VALUES (306, '丽江市', 305);
INSERT INTO `user_city` VALUES (307, '普洱市', 306);
INSERT INTO `user_city` VALUES (308, '临沧市', 307);
INSERT INTO `user_city` VALUES (309, '德宏傣族景颇族自治州', 308);
INSERT INTO `user_city` VALUES (310, '怒江傈僳族自治州', 309);
INSERT INTO `user_city` VALUES (311, '迪庆藏族自治州', 310);
INSERT INTO `user_city` VALUES (312, '大理白族自治州', 311);
INSERT INTO `user_city` VALUES (313, '楚雄彝族自治州', 312);
INSERT INTO `user_city` VALUES (314, '红河哈尼族彝族自治州', 313);
INSERT INTO `user_city` VALUES (315, '文山壮族苗族自治州', 314);
INSERT INTO `user_city` VALUES (316, '西双版纳傣族自治州', 315);
INSERT INTO `user_city` VALUES (317, '其他', 316);
INSERT INTO `user_city` VALUES (318, '拉萨市', 26);
INSERT INTO `user_city` VALUES (319, '那曲地区', 318);
INSERT INTO `user_city` VALUES (320, '昌都地区', 319);
INSERT INTO `user_city` VALUES (321, '林芝地区', 320);
INSERT INTO `user_city` VALUES (322, '山南地区', 321);
INSERT INTO `user_city` VALUES (323, '日喀则地区', 322);
INSERT INTO `user_city` VALUES (324, '阿里地区', 323);
INSERT INTO `user_city` VALUES (325, '其他', 324);
INSERT INTO `user_city` VALUES (326, '西安市', 27);
INSERT INTO `user_city` VALUES (327, '铜川市', 326);
INSERT INTO `user_city` VALUES (328, '宝鸡市', 327);
INSERT INTO `user_city` VALUES (329, '咸阳市', 328);
INSERT INTO `user_city` VALUES (330, '渭南市', 329);
INSERT INTO `user_city` VALUES (331, '延安市', 330);
INSERT INTO `user_city` VALUES (332, '汉中市', 331);
INSERT INTO `user_city` VALUES (333, '榆林市', 332);
INSERT INTO `user_city` VALUES (334, '安康市', 333);
INSERT INTO `user_city` VALUES (335, '商洛市', 334);
INSERT INTO `user_city` VALUES (336, '其他', 335);
INSERT INTO `user_city` VALUES (337, '兰州市', 28);
INSERT INTO `user_city` VALUES (338, '嘉峪关市', 337);
INSERT INTO `user_city` VALUES (339, '金昌市', 338);
INSERT INTO `user_city` VALUES (340, '白银市', 339);
INSERT INTO `user_city` VALUES (341, '天水市', 340);
INSERT INTO `user_city` VALUES (342, '武威市', 341);
INSERT INTO `user_city` VALUES (343, '酒泉市', 342);
INSERT INTO `user_city` VALUES (344, '张掖市', 343);
INSERT INTO `user_city` VALUES (345, '庆阳市', 344);
INSERT INTO `user_city` VALUES (346, '平凉市', 345);
INSERT INTO `user_city` VALUES (347, '定西市', 346);
INSERT INTO `user_city` VALUES (348, '陇南市', 347);
INSERT INTO `user_city` VALUES (349, '临夏回族自治州', 348);
INSERT INTO `user_city` VALUES (350, '甘南藏族自治州', 349);
INSERT INTO `user_city` VALUES (351, '其他', 350);
INSERT INTO `user_city` VALUES (352, '西宁市', 29);
INSERT INTO `user_city` VALUES (353, '海东地区', 352);
INSERT INTO `user_city` VALUES (354, '海北藏族自治州', 353);
INSERT INTO `user_city` VALUES (355, '海南藏族自治州', 354);
INSERT INTO `user_city` VALUES (356, '黄南藏族自治州', 355);
INSERT INTO `user_city` VALUES (357, '果洛藏族自治州', 356);
INSERT INTO `user_city` VALUES (358, '玉树藏族自治州', 357);
INSERT INTO `user_city` VALUES (359, '海西蒙古族藏族自治州', 358);
INSERT INTO `user_city` VALUES (360, '其他', 359);
INSERT INTO `user_city` VALUES (361, '银川市', 30);
INSERT INTO `user_city` VALUES (362, '石嘴山市', 361);
INSERT INTO `user_city` VALUES (363, '吴忠市', 362);
INSERT INTO `user_city` VALUES (364, '固原市', 363);
INSERT INTO `user_city` VALUES (365, '中卫市', 364);
INSERT INTO `user_city` VALUES (366, '其他', 365);
INSERT INTO `user_city` VALUES (367, '乌鲁木齐市', 31);
INSERT INTO `user_city` VALUES (368, '克拉玛依市', 367);
INSERT INTO `user_city` VALUES (369, '吐鲁番地区', 368);
INSERT INTO `user_city` VALUES (370, '哈密地区', 369);
INSERT INTO `user_city` VALUES (371, '和田地区', 370);
INSERT INTO `user_city` VALUES (372, '阿克苏地区', 371);
INSERT INTO `user_city` VALUES (373, '喀什地区', 372);
INSERT INTO `user_city` VALUES (374, '克孜勒苏柯尔克孜自治', 373);
INSERT INTO `user_city` VALUES (375, '巴音郭楞蒙古自治州', 374);
INSERT INTO `user_city` VALUES (376, '昌吉回族自治州', 375);
INSERT INTO `user_city` VALUES (377, '博尔塔拉蒙古自治州', 376);
INSERT INTO `user_city` VALUES (378, '石河子', 377);
INSERT INTO `user_city` VALUES (379, '阿拉尔', 378);
INSERT INTO `user_city` VALUES (380, '图木舒克', 379);
INSERT INTO `user_city` VALUES (381, '五家渠', 380);
INSERT INTO `user_city` VALUES (382, '伊犁哈萨克自治州', 381);
INSERT INTO `user_city` VALUES (383, '其他', 382);
INSERT INTO `user_city` VALUES (384, '台北市', 32);
INSERT INTO `user_city` VALUES (385, '新北市', 384);
INSERT INTO `user_city` VALUES (386, '桃园市', 385);
INSERT INTO `user_city` VALUES (387, '台中市', 386);
INSERT INTO `user_city` VALUES (388, '台南市', 387);
INSERT INTO `user_city` VALUES (389, '高雄市', 388);
INSERT INTO `user_city` VALUES (390, '澳门', 33);
INSERT INTO `user_city` VALUES (391, '香港', 34);

-- ----------------------------
-- Table structure for user_info
-- ----------------------------
DROP TABLE IF EXISTS `user_info`;
CREATE TABLE `user_info`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(40) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `sex` tinyint(1) NOT NULL,
  `level` int(11) NOT NULL,
  `email` varchar(40) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `icon` varchar(80) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `one` varchar(50) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `integral` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Records of user_info
-- ----------------------------
INSERT INTO `user_info` VALUES (1, 'raobaoshi', 0, 1, NULL, '6b3ceda2-f58f-4b0b-b7d5-b13812f2b4fc.jpg', NULL, 13);

-- ----------------------------
-- Table structure for user_province
-- ----------------------------
DROP TABLE IF EXISTS `user_province`;
CREATE TABLE `user_province`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `province_name` varchar(10) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 35 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Records of user_province
-- ----------------------------
INSERT INTO `user_province` VALUES (1, '北京市');
INSERT INTO `user_province` VALUES (2, '天津市');
INSERT INTO `user_province` VALUES (3, '河北省');
INSERT INTO `user_province` VALUES (4, '山西省');
INSERT INTO `user_province` VALUES (5, '内蒙古');
INSERT INTO `user_province` VALUES (6, '辽宁省');
INSERT INTO `user_province` VALUES (7, '吉林省');
INSERT INTO `user_province` VALUES (8, '黑龙江省');
INSERT INTO `user_province` VALUES (9, '上海市');
INSERT INTO `user_province` VALUES (10, '江苏省');
INSERT INTO `user_province` VALUES (11, '浙江省');
INSERT INTO `user_province` VALUES (12, '安徽省');
INSERT INTO `user_province` VALUES (13, '福建省');
INSERT INTO `user_province` VALUES (14, '江西省');
INSERT INTO `user_province` VALUES (15, '山东省');
INSERT INTO `user_province` VALUES (16, '河南省');
INSERT INTO `user_province` VALUES (17, '湖北省');
INSERT INTO `user_province` VALUES (18, '湖南省');
INSERT INTO `user_province` VALUES (19, '广东省');
INSERT INTO `user_province` VALUES (20, '广西');
INSERT INTO `user_province` VALUES (21, '海南省');
INSERT INTO `user_province` VALUES (22, '重庆市');
INSERT INTO `user_province` VALUES (23, '四川省');
INSERT INTO `user_province` VALUES (24, '贵州省');
INSERT INTO `user_province` VALUES (25, '云南省');
INSERT INTO `user_province` VALUES (26, '西藏');
INSERT INTO `user_province` VALUES (27, '陕西省');
INSERT INTO `user_province` VALUES (28, '甘肃省');
INSERT INTO `user_province` VALUES (29, '青海省');
INSERT INTO `user_province` VALUES (30, '宁夏');
INSERT INTO `user_province` VALUES (31, '新疆');
INSERT INTO `user_province` VALUES (32, '台湾省');
INSERT INTO `user_province` VALUES (33, '澳门');
INSERT INTO `user_province` VALUES (34, '香港');

-- ----------------------------
-- Table structure for user_user
-- ----------------------------
DROP TABLE IF EXISTS `user_user`;
CREATE TABLE `user_user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `telephone` varchar(11) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `password` varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `regist_time` datetime(6) NOT NULL,
  `one` varchar(50) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `telephone`(`telephone`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Records of user_user
-- ----------------------------
INSERT INTO `user_user` VALUES (1, '15755407860', 'pbkdf2:sha1:2000$3ZWSDrr7$4dad8452d5387e860318cdf5caa8d7f52f3f4a35', '2019-04-06 16:45:42.768637', '');

SET FOREIGN_KEY_CHECKS = 1;
