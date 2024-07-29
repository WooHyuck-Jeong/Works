// using System.Collections;
// using System.Collections.Generic;
// using System.IO;
// using UnityEngine;

// public class BuoyancyAUV : MonoBehaviour
// {
//     public GameObject weight;
//     public float weightMoveSpeed = 0.02f; // 속도 조절
//     public float rotationSpeed = 5f;
//     public float writeInterval = 1f; // 데이터 쓰기 간격 (초 단위)
//     public float waterLevel = 0.0f;  // 물의 표면 높이 (Y 축 기준)
//     public float floatHeight = 1.0f; // 오브젝트가 물 위에 떠있을 때의 높이
//     public float buoyancyDamping = 0.05f; // 부력 감쇠 계수
//     public float buoyancyStrength = 10.0f; // 부력 강도

//     private float auvMass = 280f;
//     private float weightMass = 42f;
//     private Vector3 weightInitialPosition;
//     private Vector3 centerOfMass;
//     private string filePath;
//     private float timer = 0f;
//     private float previousTime = 0f; // 이전 시간 저장 변수 추가

//     private Rigidbody rb;

//     void Start()
//     {
//         rb = GetComponent<Rigidbody>();

//         // 초기 위치 설정
//         transform.localScale = new Vector3(2.7f, 0.162f, 0.162f);
//         transform.position = new Vector3(0, 0, 0);

//         weight.transform.localScale = new Vector3(0.3f, 0.5f, 0.6f);
//         weightInitialPosition = new Vector3(0, 0.131f, 0);
//         weight.transform.localPosition = weightInitialPosition;

//         // 파일 경로 설정
//         filePath = Path.Combine(Application.dataPath, "SimulationResult.csv");

//         // CSV 파일 헤더 작성
//         WriteHeaderToFile();
//     }

//     void Update()
//     {
//         MoveWeight();
//         UpdateAUVRotation();
//         CalculateCenterOfMass();
//         DisplayInfo();

//         timer += Time.deltaTime;
//         if (timer >= writeInterval)
//         {
//             WriteDataToFile();
//             timer = 0f; // 타이머 리셋
//         }
//     }

//     void FixedUpdate()
//     {
//         ApplyBuoyancy();
//     }

//     void MoveWeight()
//     {
//         Vector3 localPos = weight.transform.localPosition;

//         if (Input.GetKey(KeyCode.LeftArrow))
//         {
//             localPos.x -= weightMoveSpeed * Time.deltaTime;
//         }
//         if (Input.GetKey(KeyCode.RightArrow))
//         {
//             localPos.x += weightMoveSpeed * Time.deltaTime;
//         }

//         // 무게추가 AUV의 윗면에 있도록 제한
//         localPos.x = Mathf.Clamp(localPos.x, -2.4f, 2.4f);
//         localPos.y = 0.55f;
//         localPos.z = 0;

//         weight.transform.localPosition = localPos;
//     }

//     void UpdateAUVRotation()
//     {
//         Vector3 weightLocalPosition = weight.transform.localPosition;
//         float distanceFromCenter = weightLocalPosition.x;

//         // 무게 중심 이동에 따른 토크 계산
//         float torque = distanceFromCenter * weightMass;

//         // Z 축을 기준으로 회전 적용
//         transform.Rotate(0, 0, -torque * rotationSpeed * Time.deltaTime);
//     }

//     void CalculateCenterOfMass()
//     {
//         Vector3 auvPosition = transform.position;
//         Vector3 weightPosition = weight.transform.position;

//         // 무게 중심 계산
//         centerOfMass = (auvPosition * auvMass + weightPosition * weightMass) / (auvMass + weightMass);
//     }

//     void DisplayInfo()
//     {
//         float rotationAngle = transform.eulerAngles.z;
//         if (rotationAngle > 180f)
//         {
//             rotationAngle -= 360f;
//         }

//         rotationAngle = Mathf.Abs(rotationAngle);

//         Vector3 weightPosition = weight.transform.position;

//         // 콘솔에 정보 표시
//         Debug.Log($"Center of Mass: {centerOfMass}");
//         Debug.Log($"AUV Rotation Angle: {rotationAngle} degrees");
//         Debug.Log($"Weight Position: {weightPosition}");
//     }

//     void WriteDataToFile()
//     {
//         float currentTime = Time.time;
//         float rotationAngle = transform.eulerAngles.z;
//         if (rotationAngle > 180f)
//         {
//             rotationAngle -= 360f;
//         }

//         rotationAngle = Mathf.Abs(rotationAngle);
//         if (rotationAngle == 360f)
//         {
//             rotationAngle = 0f;
//         }

//         Vector3 weightPosition = weight.transform.position;
//         // 이전 시간과 현재 시간이 다를 때만 데이터 기록
//         if (currentTime != previousTime)
//         {
//             string data = $"{currentTime},{centerOfMass.x},{centerOfMass.y},{centerOfMass.z},{rotationAngle},{weightPosition.x},{weightPosition.y},{weightPosition.z}";
//             WriteToFile(data);
//             previousTime = currentTime;
//         }
//     }

//     void WriteHeaderToFile()
//     {
//         try
//         {
//             using (StreamWriter writer = new StreamWriter(filePath, false))
//             {
//                 writer.WriteLine("Time,CenterOfMassX,CenterOfMassY,CenterOfMassZ,RotationAngle,WeightPositionX,WeightPositionY,WeightPositionZ");
//             }
//         }
//         catch (System.Exception e)
//         {
//             Debug.LogError("Error writing to file: " + e.Message);
//         }
//     }

//     void WriteToFile(string data)
//     {
//         try
//         {
//             using (StreamWriter writer = new StreamWriter(filePath, true))
//             {
//                 writer.WriteLine(data);
//             }
//         }
//         catch (System.Exception e)
//         {
//             Debug.LogError("Error writing to file: " + e.Message);
//         }
//     }

//     void ApplyBuoyancy()
//     {
//         // 물 표면에서의 거리
//         float difference = transform.position.y - waterLevel;

//         // 중성부력 상태 유지
//         if (difference < floatHeight)
//         {
//             float forceFactor = 1.0f - (difference / floatHeight);
//             Vector3 upwardForce = -Physics.gravity * (forceFactor - rb.velocity.y * buoyancyDamping);
//             upwardForce.y = Mathf.Clamp(upwardForce.y, 0, buoyancyStrength);

//             rb.AddForce(upwardForce, ForceMode.Acceleration);
//         }
//     }
// }


using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEngine;

public class BuoyancyAUV : MonoBehaviour
{
    public GameObject weight;
    public float weightMoveSpeed = 0.02f; // 속도 조절
    public float rotationSpeed = 5f;
    public float writeInterval = 1f; // 데이터 쓰기 간격 (초 단위)
    public float waterLevel = 0.0f;  // 물의 표면 높이 (Y 축 기준)
    public float floatHeight = 1.0f; // 오브젝트가 물 위에 떠있을 때의 높이
    public float buoyancyDamping = 0.05f; // 부력 감쇠 계수
    public float buoyancyStrength = 10.0f; // 부력 강도
    public float angularDamping = 0.1f; // 각속도 감쇠 계수

    private float auvMass = 280f;
    private float weightMass = 42f;
    private Vector3 weightInitialPosition;
    private Vector3 centerOfMass;
    private string filePath;
    private float timer = 0f;
    private float previousTime = 0f; // 이전 시간 저장 변수 추가

    private Rigidbody rb;

    void Start()
    {
        rb = GetComponent<Rigidbody>();

        // 초기 위치 설정
        transform.localScale = new Vector3(2.7f, 0.162f, 0.162f);
        transform.position = new Vector3(0, 0, 0);

        weight.transform.localScale = new Vector3(0.3f, 0.5f, 0.6f);
        weightInitialPosition = new Vector3(0, 0.131f, 0);
        weight.transform.localPosition = weightInitialPosition;

        // 파일 경로 설정
        filePath = Path.Combine(Application.dataPath, "SimulationResult.csv");

        // CSV 파일 헤더 작성
        // WriteHeaderToFile();
    }

    void Update()
    {
        MoveWeight();
        CalculateCenterOfMass();
        DisplayInfo();

        // timer += Time.deltaTime;
        // if (timer >= writeInterval)
        // {
        //     WriteDataToFile();
        //     timer = 0f; // 타이머 리셋
        // }
    }

    void FixedUpdate()
    {
        ApplyBuoyancy();
        ApplyAngularDamping();
        UpdateAUVRotation();
    }

    void MoveWeight()
    {
        Vector3 localPos = weight.transform.localPosition;

        if (Input.GetKey(KeyCode.LeftArrow))
        {
            localPos.x += weightMoveSpeed * Time.deltaTime;
        }
        if (Input.GetKey(KeyCode.RightArrow))
        {
            localPos.x -= weightMoveSpeed * Time.deltaTime;
        }

        // 무게추가 AUV의 윗면에 있도록 제한
        localPos.x = Mathf.Clamp(localPos.x, -2.4f, 2.4f);
        localPos.y = 0.55f;
        localPos.z = 0;

        weight.transform.localPosition = localPos;
    }

    void UpdateAUVRotation()
    {
        Vector3 weightLocalPosition = weight.transform.localPosition;
        float distanceFromCenter = weightLocalPosition.x;

        // 무게 중심 이동에 따른 토크 계산
        float torque = distanceFromCenter * weightMass;

        // Z 축을 기준으로 회전 적용
        // rb.AddTorque(new Vector3(0, 0, -torque * rotationSpeed * Time.fixedDeltaTime), ForceMode.Force);
        rb.AddTorque(new Vector3(0, 0, -torque * rotationSpeed * Time.fixedDeltaTime), ForceMode.Acceleration);
    }

    void CalculateCenterOfMass()
    {
        Vector3 auvPosition = transform.position;
        Vector3 weightPosition = weight.transform.position;

        // 무게 중심 계산
        centerOfMass = (auvPosition * auvMass + weightPosition * weightMass) / (auvMass + weightMass);
    }

    void DisplayInfo()
    {
        float rotationAngle = transform.eulerAngles.z;
        if (rotationAngle > 180f)
        {
            rotationAngle -= 360f;
        }

        Vector3 weightPosition = weight.transform.position;

        // 콘솔에 정보 표시
        Debug.Log($"Center of Mass: {centerOfMass}");
        Debug.Log($"AUV Rotation Angle: {rotationAngle} degrees");
        Debug.Log($"Weight Position: {weightPosition}");
    }

    // void WriteDataToFile()
    // {
    //     float currentTime = Time.time;
    //     float rotationAngle = transform.eulerAngles.z;
    //     if (rotationAngle > 180f)
    //     {
    //         rotationAngle -= 360f;
    //     }

    //     Vector3 weightPosition = weight.transform.position;
    //     // 이전 시간과 현재 시간이 다를 때만 데이터 기록
    //     if (currentTime != previousTime)
    //     {
    //         string data = $"{currentTime},{centerOfMass.x},{centerOfMass.y},{centerOfMass.z},{rotationAngle},{weightPosition.x},{weightPosition.y},{weightPosition.z}";
    //         WriteToFile(data);
    //         previousTime = currentTime;
    //     }
    // }

    // void WriteHeaderToFile()
    // {
    //     try
    //     {
    //         using (StreamWriter writer = new StreamWriter(filePath, false))
    //         {
    //             writer.WriteLine("Time,CenterOfMassX,CenterOfMassY,CenterOfMassZ,RotationAngle,WeightPositionX,WeightPositionY,WeightPositionZ");
    //         }
    //     }
    //     catch (System.Exception e)
    //     {
    //         Debug.LogError("Error writing to file: " + e.Message);
    //     }
    // }

    // void WriteToFile(string data)
    // {
    //     try
    //     {
    //         using (StreamWriter writer = new StreamWriter(filePath, true))
    //         {
    //             writer.WriteLine(data);
    //         }
    //     }
    //     catch (System.Exception e)
    //     {
    //         Debug.LogError("Error writing to file: " + e.Message);
    //     }
    // }

    void ApplyBuoyancy()
    {
        // 물 표면에서의 거리
        float difference = transform.position.y - waterLevel;

        // 중성부력 상태 유지
        if (difference < floatHeight)
        {
            float forceFactor = 1.0f - (difference / floatHeight);
            Vector3 upwardForce = -Physics.gravity * (forceFactor - rb.velocity.y * buoyancyDamping);
            upwardForce.y = Mathf.Clamp(upwardForce.y, 0, buoyancyStrength);

            rb.AddForce(upwardForce, ForceMode.Acceleration);
        }
    }

    void ApplyAngularDamping()
    {
        // 각속도 감쇠 적용
        rb.angularVelocity = new Vector3(rb.angularVelocity.x, rb.angularVelocity.y, rb.angularVelocity.z * (1 - angularDamping));
    }
}