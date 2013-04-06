
# Mozilla extension ID's and locations
%define moz_ext_dir %{_libdir}/mozilla/extensions
%define src_ext_id \{6f9d85e0-794d-11dd-ad8b-0800200c9a66\}

%define firefox_app_id \{ec8030f7-c20a-464f-9b0e-13a3a9e97384\}
%define inst_dir %{moz_ext_dir}/%{firefox_app_id}/%{src_ext_id}

#%define thunderbird_app_id \{3550f703-e582-4d05-9a08-453d09bdfdc6\}
#%define thunderbird_inst_dir %{moz_ext_dir}/%{thunderbird_app_id}/%{src_ext_id}
#
#%define seamonkey_app_id \{92650c4d-4b8e-4d2a-b7eb-24ecf4f6b63a\}
#%define seamonkey_inst_dir %{moz_ext_dir}/%{seamonkey_app_id}/%{src_ext_id}


%global github_owner infinity0

%global commit 32f04a6a2377e5af354120c1a64b9ec4f9e8eef1
%global shortcommit %(c=%{commit}; echo ${c:0:7})


Name:		mozilla-gnome-keyring
Version:	0.6.8
Release:	2%{?dist}
Summary:	Store mozilla passwords in GNOME Keyring

Group:		Applications/Internet
License:	MPLv1.1
URL:		https://github.com/infinity0/mozilla-gnome-keyring
Source0:    https://github.com/%{github_owner}/%{name}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

BuildRequires:	xulrunner-devel, libgnome-keyring-devel
Requires:	mozilla-filesystem

%description
This extension integrates gnome-keyring into Firefox applications as 
the software security device.


%prep
%setup -q -n %{name}-%{commit}


%build
make %{?_smp_mflags} VERSION=%{version}


%install
# clean buildroot
rm -rf %{buildroot}

# install extension
install -dm 755 %{buildroot}%{inst_dir}
cd xpi/
install -Dpm 644 chrome.manifest install.rdf %{buildroot}%{inst_dir}
install -dm 755 %{buildroot}%{inst_dir}/platform/Linux_%{_arch}-gcc3/components/
install -pm 644 --strip platform/Linux_%{_arch}-gcc3/components/libgnomekeyring.so %{buildroot}%{inst_dir}/platform/Linux_%{_arch}-gcc3/components/

## symlink from seamonkey extension to firefox extension
#mkdir -p %{buildroot}%{moz_ext_dir}/%{seamonkey_app_id}
#ln -s %{inst_dir} %{buildroot}%{seamonkey_inst_dir}

## symlink from thunderbird extension to firefox extension
#mkdir -p %{buildroot}%{moz_ext_dir}/%{thunderbird_app_id}
#ln -s %{inst_dir} %{buildroot}%{thunderbird_inst_dir}

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{inst_dir}
#%{thunderbird_inst_dir}
#%{seamonkey_inst_dir}
%doc README AUTHORS COPYING LICENSE.GPL-2 LICENSE.LGPL-2.1 LICENSE.MPL-1.1


%changelog
* Sat Apr 06 2013 Alexander Korsunsky <fat.lobyte9@gmail.com> - 0.6.8-2
- Rebuild for Firefox 20

* Sat Feb 23 2013 Alexander Korsunsky <fat.lobyte9@gmail.com> - 0.6.8-1
- Initial Release
