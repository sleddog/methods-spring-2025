use std::process::Command;

#[test]
fn test_bobcat_for_1() {
    let output = Command::new("cargo")
        .args(&["run", "--quiet", "--", "1"])
        .output()
        .expect("Failed to execute process");

    assert_eq!(String::from_utf8_lossy(&output.stdout).trim(), "1");
}

#[test]
fn test_bobcat_for_3() {
    let output = Command::new("cargo")
        .args(&["run", "--quiet", "--", "3"])
        .output()
        .expect("Failed to execute process");

    assert_eq!(
        String::from_utf8_lossy(&output.stdout).trim(),
        "1\n2\nBob"
    );
}

#[test]
fn test_bobcat_for_5() {
    let output = Command::new("cargo")
        .args(&["run", "--quiet", "--", "5"])
        .output()
        .expect("Failed to execute process");

    assert_eq!(
        String::from_utf8_lossy(&output.stdout).trim(),
        "1\n2\nBob\n4\nCat"
    );
}

#[test]
fn test_bobcat_for_15() {
    let output = Command::new("cargo")
        .args(&["run", "--quiet", "--", "15"])
        .output()
        .expect("Failed to execute process");

    assert_eq!(
        String::from_utf8_lossy(&output.stdout).trim(),
        "1\n2\nBob\n4\nCat\nBob\n7\n8\nBob\nCat\n11\nBob\n13\n14\nBobCat"
    );
}
