# Placeholder spec for piloting the Fedora workflows (Fedora Task 01-05).
# The real spec, including Requires: regolith-wm-config once that package is
# in regolith-unstable, comes from Fedora Task 05-06.

Name:           regolith-sway-touchpad-gestures
Version:        0.1.0
Release:        0.2%{?dist}
Summary:        Sway configuration that enables touchpad gestures for Regolith

License:        MIT
URL:            https://github.com/regolith-linux/regolith-sway-touchpad-gestures
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

%description
Sway configuration partial that maps touchpad swipe gestures to workspace
navigation in the Regolith desktop.

%prep
%autosetup

%build

%install
install -Dpm 0644 usr/share/regolith/sway/config.d/61_touchpad_guestures \
    %{buildroot}%{_datadir}/regolith/sway/config.d/61_touchpad_guestures

%files
%dir %{_datadir}/regolith
%dir %{_datadir}/regolith/sway
%dir %{_datadir}/regolith/sway/config.d
%{_datadir}/regolith/sway/config.d/61_touchpad_guestures

%changelog
* Tue Nov 03 2026 Joseph Moon <joemoonmeta@meta.com> - 0.1.0-0.2
- Bump the release to test fedora-prepare-release (Fedora Task 01-05)

* Wed Oct 14 2026 Joseph Moon <joemoonmeta@meta.com> - 0.1.0-0.1
- Placeholder package for the Fedora workflow pilot
