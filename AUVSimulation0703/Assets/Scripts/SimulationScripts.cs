using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEngine;

public class SimulationScrips : MonoBehaviour
{
    
    public GameObject weight;
    public float weightMoveSpeed = 0.01f;       // [m]
    public float rotationSpeed = 5;             // [m/s]
    public float waterLevel = 0.0f;             // 자유수면 높이 (y축 기준)
    public float floatHeight = 1.0f;            // 오브젝트가 물 위에 떠 있을 때의 높이
    public float buoyancyDamping = 0.05f;       // 부력 감쇠 계수
    public float buoyancyStrength = 10.0f;      // 부력 강도
    public float angularDamping = 0.1f;         // 각속도 감쇠 계수

    private float auvMass = 238f;
    private float weightMass = 42f;
    private Vector3 weightInitialPosition;
    private Vector3 centerOfMass;
    
    private Rigidbody rb;

    private void Start() {
        rb = GetComponent<Rigidbody>();

        // Initial position
        transform.localScale = new Vector3(2.7f, 0.162f, 0.162f);       // AUV 사이즈
        transform.position = new Vector3(0, 0, 0);                      // AUV initial position

        weight.transform.localScale = new Vector3(0.3f, 0.5f, 0.5f);    // Weight 사이즈
        weightInitialPosition = new Vector3(0, 0.55f, 0);
        weight.transform.localPosition = weightInitialPosition;
    }

    private void Update() {
        MoveWeight();
        CalculateCenterOfMass();
        DisplayInfo();
    }

    private void FixedUpdate() {
        ApplyBuoyancy();
        // ApplyAngularDamping();
        UpdateAUVRotation();
    }

    void MoveWeight(){

        Vector3 localPos = weight.transform.localPosition;

        if (Input.GetKey(KeyCode.LeftArrow)){
            localPos.x += weightMoveSpeed * Time.deltaTime;
        }
        if (Input.GetKey(KeyCode.RightArrow)){
            localPos.x -= weightMoveSpeed * Time.deltaTime;
        }

        // 무게추 위치 제한
        localPos.x = Mathf.Clamp(localPos.x, -2.4f, 2.4f);
        localPos.y = 0.55f;
        localPos.z = 0;

        weight.transform.localPosition = localPos;
    }

    void UpdateAUVRotation(){

        Vector3 weightLocalPosition = weight.transform.localPosition;
        float distanceFromCenter = weightLocalPosition.x;

        // 무게중심 이동에 따른 토크 계산
        float torque = distanceFromCenter * weightMass;

        // z축을 기준으로 회전
        rb.AddTorque(new Vector3(0, 0, -torque * rotationSpeed * Time.deltaTime), ForceMode.Force);
    }

    void CalculateCenterOfMass(){

        Vector3 auvPosition = transform.position;
        Vector3 weightPosition = weight.transform.position;

        // 무게중심 계산
        centerOfMass = (auvPosition * auvMass + weightPosition * weightMass) / (auvMass + weightMass);
    }

    void DisplayInfo(){

        float rotationAngle = transform.eulerAngles.z;

        if (rotationAngle > 180f){
            rotationAngle -= 360f;
        }

        Vector3 weightPosition = weight.transform.position;

        // 콘솔창 출력
        Debug.Log($"Center Of Mass: {centerOfMass}");
        Debug.Log($"Rotation Angle: {rotationAngle}");
    }

    void ApplyBuoyancy(){

        // 물 표면에서의 거리
        float difference = transform.position.y - waterLevel;       // auv y좌표 - 0

        // 중성부력 상태 유지
        if (difference < floatHeight){
            float forceFactor = 1.0f - (difference / floatHeight);
            Vector3 upwardForce = -Physics.gravity * (forceFactor - rb.velocity.y * buoyancyDamping);
            upwardForce.y = Mathf.Clamp(upwardForce.y, 0, buoyancyStrength);

            rb.AddForce(upwardForce, ForceMode.Acceleration);
        }
    }
}