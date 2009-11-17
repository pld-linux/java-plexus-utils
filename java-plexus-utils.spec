# TODO:
# - package maven and THEN try to build it from sources
#
%include	/usr/lib/rpm/macros.java
#
%define		srcname		plexus-utils
%define		snap		20081115.130716
%define		snapno		4
Summary:	Utilities for plexus components
Name:		java-plexus-utils
Version:	1.5.7
Release:	0.%{snap}.0.1
License:	Apache v2.0
Group:		Libraries/Java
Source0:	http://snapshots.repository.codehaus.org/org/codehaus/plexus/plexus-utils/%{version}-SNAPSHOT/plexus-utils-%{version}-%{snap}-%{snapno}.jar
# Source0-md5:	300eafb84ffd675a613e57c577b662ae

URL:		http://plexus.codehaus.org/plexus-utils/
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	java-plexus-container
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A collection of various utility classes to ease working with strings, files,
command lines, XML and more.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}
install %{SOURCE0} $RPM_BUILD_ROOT%{_javadir}/%{srcname}-%{version}-%{snap}-%{snapno}.jar
ln -s %{srcname}-%{version}-%{snap}-%{snapno}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_javadir}/*.jar
