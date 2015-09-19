Name:           ros-jade-catkin
Version:        0.6.15
Release:        0%{?dist}
Summary:        ROS catkin package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/catkin
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       cmake
Requires:       gtest-devel
Requires:       python
Requires:       python-catkin_pkg > 0.2.9
Requires:       python-empy
Requires:       python-nose
BuildRequires:  cmake
BuildRequires:  python
BuildRequires:  python-catkin_pkg > 0.2.9
BuildRequires:  python-empy
BuildRequires:  python-mock
BuildRequires:  python-nose

%description
Low-level build system macros and infrastructure for ROS.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
#        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Sat Sep 19 2015 Dirk Thomas <dthomas@osrfoundation.org> - 0.6.15-0
- Autogenerated by Bloom

* Mon Apr 20 2015 Dirk Thomas <dthomas@osrfoundation.org> - 0.6.14-0
- Autogenerated by Bloom

* Fri Apr 17 2015 Dirk Thomas <dthomas@osrfoundation.org> - 0.6.13-0
- Autogenerated by Bloom

* Thu Apr 16 2015 Dirk Thomas <dthomas@osrfoundation.org> - 0.6.12-0
- Autogenerated by Bloom

* Mon Dec 29 2014 Dirk Thomas <dthomas@osrfoundation.org> - 0.6.11-0
- Autogenerated by Bloom

* Fri Dec 26 2014 Dirk Thomas <dthomas@osrfoundation.org> - 0.6.10-2
- Autogenerated by Bloom

* Tue Dec 23 2014 Dirk Thomas <dthomas@osrfoundation.org> - 0.6.10-1
- Autogenerated by Bloom

* Tue Dec 23 2014 Dirk Thomas <dthomas@osrfoundation.org> - 0.6.10-0
- Autogenerated by Bloom

