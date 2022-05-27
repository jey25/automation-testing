@Test

// 확인 텍스트를 가진 오브젝트를 찾아 permissionConfirmButton 에 넣고,
// permissionConfirmButton 이 Null 이 아니라면 해당 영역을 클릭한다.
// (타임 아웃 5초)


fun testInitialization() {
    val permissionConfirmButton = mDevice.wait(Until.findObject(By.textContains("확인")), 5000)
    Assert.assertNotNull(permissionConfirmButton)
    permissionConfirmButton.click()
}